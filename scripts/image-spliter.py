#!/usr/bin/env python

from PIL import Image
import argparse, pathlib, json

# See http://www.sview.ru/en/help/input/
# See https://note.nkmk.me/en/python-pillow-concat-images/
def crossed_eyed(left, right, file, format = "jpeg"):
    ce = Image.new('RGB', (right.width + left.width, right.height))
    ce.paste(right, (0, 0))
    ce.paste(left, (right.width, 0))
    ce.save(file, format)
    return ce

parser = argparse.ArgumentParser(description='Extract steroscopic images')
parser.add_argument('--image',  type=pathlib.Path, help='Image to process', required=True)
parser.add_argument('--coords',  type=pathlib.Path, help='File containing coordinates', required=True)
parser.add_argument('--output',  choices=['gif', 'jps', 'images'], help='Output format')

args = parser.parse_args()

im = Image.open(args.image)
coords = json.load(args.coords.open())

leftFileName = args.image.parent.joinpath(args.image.stem + "-left" + args.image.suffix)
rightFileName = args.image.parent.joinpath(args.image.stem + "-right" + args.image.suffix)
print("Left start position {},{}, size {}, {} - File name {}".format(coords["left"]["position"]["x"], coords["left"]["position"]["y"], coords["left"]["size"]["x"], coords["left"]["size"]["y"], leftFileName))
print("Right start position {},{}, size {}, {} - File name {}".format(coords["right"]["position"]["x"], coords["right"]["position"]["y"], coords["right"]["size"]["x"], coords["right"]["size"]["y"], rightFileName))

left_left = coords["left"]["position"]["x"]
left_top = coords["left"]["position"]["y"]
left_right = coords["left"]["size"]["x"] + coords["left"]["position"]["x"]
left_bottom = coords["left"]["size"]["y"] + coords["left"]["position"]["y"]

right_left = coords["right"]["position"]["x"]
right_top = coords["left"]["position"]["y"]
right_right = coords["right"]["size"]["x"] + coords["right"]["position"]["x"]
right_bottom =  coords["right"]["size"]["y"] + coords["right"]["position"]["y"]

if (coords["left"]["size"]["x"] != coords["right"]["size"]["x"]):
    print("Width (x) doesn't match!", end=" ")
    if (coords["left"]["size"]["x"] < coords["right"]["size"]["x"]):
        print ("Left image is narrower")
        print("Old left for right image {}, right for right image {} - width {}".format(right_left, right_right, coords["right"]["size"]["x"]))
        right_left = (coords["right"]["position"]["x"] + (coords["right"]["size"]["x"] - coords["left"]["size"]["x"]) / 2)
        right_right = coords["left"]["size"]["x"] + right_left
        print("New left for right image {}, right for right image {} - width {}".format(right_left, right_right, right_right - right_left))
    else:
        print ("Right image is narrower")
        print("Old left for left image {}, right for left image {} - width {}".format(left_left, left_right, coords["left"]["size"]["x"]))
        left_left = coords["left"]["position"]["x"] + ((coords["left"]["size"]["x"] - coords["right"]["size"]["x"]) / 2)
        left_right = coords["right"]["size"]["x"] + left_left # change
        print("New left for left image {}, right for left image {} - width {}".format(left_left, left_right, left_right - left_left))


if ( coords["left"]["size"]["y"] != coords["right"]["size"]["y"]):
    print("Height (y) doesn't match!", end=" ")

    if (coords["left"]["size"]["y"] < coords["right"]["size"]["y"]):
        print ("Left image is smaller")
        print("Old top for right image {}, bottom for right image {}".format(right_top, right_bottom))
        right_top = (coords["right"]["position"]["y"] + (coords["right"]["size"]["y"] - coords["left"]["size"]["y"]) / 2)
        right_bottom = coords["left"]["size"]["y"] + right_top
        print("New top for right image {}, bottom for right image {}".format(right_top, right_bottom))
    else:
        print ("Right image is smaller")
        print("Old top for left image {}, bottom for left image {}".format(left_top, left_bottom))
        left_top = (coords["left"]["position"]["y"] + (coords["left"]["size"]["y"] - coords["right"]["size"]["y"]) / 2)
        left_bottom = coords["right"]["size"]["y"] + left_top
        print("New top for left image {}, bottom for left image {}".format(left_top, left_bottom))


left = im.crop((left_left, left_top, left_right, left_bottom))
right = im.crop((right_left, right_top, right_right, right_bottom))

# See https://blog.miguelgrinberg.com/post/take-3d-pictures-with-your-canon-dslr-and-magic-lantern

if (args.output == "gif"):
    gifFileName = args.image.parent.joinpath(args.image.stem + ".gif")
    left.save(gifFileName, save_all=True, append_images=[right], duration=0.1, loop=0, dispose=2)
elif (args.output == "jps"):
    ceFileName = args.image.parent.joinpath(args.image.stem + ".jps")
    crossed_eyed(left, right, ceFileName)
else:
    left.save(leftFileName)
    right.save(rightFileName)
