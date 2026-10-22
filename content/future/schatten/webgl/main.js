import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { FontLoader } from 'three/addons/loaders/FontLoader.js';
import { TextGeometry } from 'three/addons/geometries/TextGeometry.js';

THREE.Cache.enabled = true;

const url = './model.glb';

function createArray(x, y, z, dist, intensity) {
  const group = new THREE.Group();
  for (let i = 0; i < x; i++) {
    for (let j = 0; i < y; i++) {

      const spotLight = new THREE.SpotLight(0xffffff, intensity);
      spotLight.position.set(i * dist, j * dist, z);

      spotLight.castShadow = true;

      spotLight.shadow.mapSize.width = 1024;
      spotLight.shadow.mapSize.height = 1024;

      spotLight.shadow.camera.near = 500;
      spotLight.shadow.camera.far = 4000;
      spotLight.shadow.camera.fov = 30;
      //const spotLightHelper = new THREE.SpotLightHelper( spotLight );
      group.add(spotLight);
    }
  }
  return group;
}

function writeText(text) {

}

var array = createArray(0, 0, 0, .5, 10);
array.position.setZ(5);

const scene = new THREE.Scene();
scene.background = new THREE.Color( 0x000000 );
scene.fog = new THREE.Fog( 0x000000, 250, 1400 );

const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );
camera.position.set( 0, 400, 700 );

const renderer = new THREE.WebGLRenderer();
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
const controls = new OrbitControls( camera, renderer.domElement );

//const loader = new GLTFLoader();


const light = new THREE.AmbientLight( 0x404040 ); // soft white light
scene.add( light );

scene.add(array);

renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

/*
loader.load(url, function (gltf) {
  scene.add( gltf.scene );
}, undefined, function ( error ) {
  console.error( error );
});
*/

controls.update();

function animate() {
	requestAnimationFrame( animate );
  controls.update();
	renderer.render( scene, camera );
}

animate();
