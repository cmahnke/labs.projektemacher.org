#!/usr/bin/env python

# TODO:
# * scale embedded icon, see https://github.com/lincolnloop/python-qrcode/blob/master/qrcode/image/styledpil.py#L85
# * Clip QR Code

import qrcode, json, re, os
import argparse, pathlib
import svgutils.transform
from termcolor import cprint
from os.path import exists
import qrcode.image.svg
from qrcode.image.pil import PilImage
from qrcode.image.styledpil import StyledPilImage
from cairosvg import svg2png
import xml.etree.ElementTree as ET
from svgutils.compose import Unit
from svgutils.transform import GroupElement, FigureElement

defaultOutfile = "qrcode.svg"
contentPath = "./docs"
filePattern = "qrcode.json"
factory = 'svg'
height = '10cm'
width = '10cm'

parser = argparse.ArgumentParser(prog = 'generate-qr-codes.py', description = 'Generate QR Code')
parser.add_argument('-i', '--include', '--icon', metavar="[include path]", type=pathlib.Path, help="Path to include icons from")
parser.add_argument('-o', '--output', metavar="filename", help="Output file name, defaults to '{}'".format(defaultOutfile))
parser.add_argument('-b', '--background', choices=['square', 'circle'], help="Background primitive for icon")
args = parser.parse_args()

if args.output is not None:
    outfile = vars(args).output
else:
    outfile = defaultOutfile

if (factory == 'svg'):
    factory = qrcode.image.svg.SvgPathImage
else:
    factory = PilImage
    raise ValueError("Generating QR Codes using PIL isn't supported anymore")

# Setup XML parser
namespaces = {'svg': 'http://www.w3.org/2000/svg', 'xlink': 'http://www.w3.org/1999/xlink',
'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#', 'dc': 'http://purl.org/dc/elements/1.1/', 'cc': 'http://creativecommons.org/ns#'}
for prefix, namespace in namespaces.items():
    ET.register_namespace(prefix, namespace)

# SVG Primitives
primitives = {}
primitives['circle'] = """
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="50" r="50" fill="white" />
</svg>
"""
primitives['square'] = """
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <rect width="100" height="100" fill="white" />
</svg>
"""

# Functions
def setPathFill(svgStr, color):
    root = ET.fromstring(svgStr)
    for elem in root.findall('.//{%s}path'%(namespaces["svg"])):
       elem.set('fill', color)
    return ET.tostring(root, encoding='utf8', method='xml').decode('utf-8')

def getSize(svgStr):
    root = ET.fromstring(svgStr)
    return {'height': root.get('height'), 'width': root.get('width')}

def calculateMargin(width, scale):
    backgroundScale = 0.75
    objWidth = BetterUnit(width) * scale
    margin = (BetterUnit(width) - objWidth) / 2
    return margin.value

# Classes
class BetterUnit (Unit):
    def __init__(self, measure):
        if measure.endswith('%'):
            m = re.match("([0-9]+\.?[0-9]*)(%)", measure)
            value, unit = m.groups()
            self.value = float(value)
            self.unit = unit
        else:
            Unit.__init__(self, measure)

    def __sub__(self, number):
        if isinstance(number, Unit):
            if self.unit == number.unit:
                return BetterUnit(str(self.value - number.value) + self.unit)
            else:
                raise ValueError('Can\'t calculate with different units: Having \'{}\', got \'{}\''.format(self.unit, number.unit))
        elif isinstance(number, int):
            return BetterUnit(str(self.value - number) + self.unit)
        else:
            raise TypeError('Only \'Unit\' ant \'int\' are supported, not \'{}\''.format(type(number)))

    def __add__(self, number):
        if isinstance(number, Unit):
            if self.unit == number.unit:
                return BetterUnit(str(self.value + number.value) + self.unit)
            else:
                raise ValueError('Can\'t calculate with different units: Having \'{}\', got \'{}\''.format(self.unit, number.unit))
        elif isinstance(number, int):
            return BetterUnit(str(self.value + number) + self.unit)
        else:
            raise TypeError('Only \'Unit\' ant \'int\' are supported, not \'{}\''.format(type(number)))

#def scale(svgStr, factor):
#    root = ET.fromstring(svgStr)
#    svgutils.transform.FigureElement(root[0]).scale(factor)

# Documentation QR Codes: https://pypi.org/project/qrcode/
# Documentation SVG to PNG: https://cairosvg.org/documentation/
# Documentation Mxerge SVGs: https://svgutils.readthedocs.io/en/latest/index.html

cFilePAttern = re.compile(filePattern)
for subdir, dirs, files in os.walk(contentPath):
    for file in files:
        fileMatch = cFilePAttern.match(file)
        if fileMatch:
            cprint("Processing " + os.path.join(subdir, file), 'green')
            with open(os.path.join(subdir, file), 'r') as f:
                data = json.load(f)

            img = qrcode.make(data['url'], image_factory=factory)
            svg = img.to_string().decode('utf-8')
            size = getSize(svg)
            #cprint("Size is {} by {}".format(size["width"], size["height"]), 'yellow')
            if "color" in data:
                svg = setPathFill(svg, data['color'])
            if "icon" in data:
                iconFile = data['icon']
                if args.include is not None:
                    iconFile = os.path.join(args.include, iconFile)
                if not exists(iconFile):
                    raise ValueError(f'Icon file \'{iconFile}\' doesn\'t exist!')

                if iconFile.endswith('svg') and exists(iconFile):
                    cprint("Using icon " + iconFile, 'green')
                    #PIL.Image.open(io.BytesIO(svg2png(url=filename, write_to=None)))
                    # Merge SVGs https://stackoverflow.com/a/23482756
                    svgTemplate = svgutils.transform.fromstring(svg)
                    icon = svgutils.transform.fromfile(iconFile)
                    if "iconColor" in data:
                        iconSvg = icon.tostr().decode('utf-8')
                        iconSvg = setPathFill(iconSVG, data['iconColor'])
                        icon = svgutils.transform.fromstring(iconSvg)
                    background = None
                    if args.background is not None:
                        background = args.background
                    if "background" in data:
                        background = data['background']

                    if background is not None and background in primitives:
                        backgroundTemplate = svgutils.transform.fromstring(primitives[background])
                        backgroundScale = 0.75
                        margin = calculateMargin(size["width"], backgroundScale)
                        icon = GroupElement([icon.root])
                        icon.moveto(margin, margin, scale_x=backgroundScale)
                        backgroundTemplate = FigureElement(backgroundTemplate.root)
                        icon = GroupElement([backgroundTemplate, icon])
                    elif background is not None:
                        cprint("Background set to '{}', but no primitive found by this name".format(background), red)
                    else:
                        icon = GroupElement([icon.root])

                    icon = GroupElement(icon.root)
                    iconScale = 0.4
                    margin = calculateMargin(size["width"], iconScale)
                    icon.moveto(margin, margin, scale_x=iconScale)
                    svgTemplate.append(icon)
                    svg = svgTemplate.to_str().decode('utf-8')
                else:
                    raise ValueError("Embedding Icon as raster image isn't supported!")
                    #img = qr.make_image(image_factory=StyledPilImage, embeded_image_path=icon)

            if outfile.endswith('svg'):
                with open(os.path.join(subdir, outfile), "w") as svg_file:
                    svg_file.write(svg)
            else:
                svg2png(bytestring=svg.encode('utf-8'), write_to=os.path.join(subdir, outfile))

            cprint("Saved file " + os.path.join(subdir, outfile), 'green')
