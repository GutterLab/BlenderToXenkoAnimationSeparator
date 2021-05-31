# BlenderToStrideAnimationSeparator
A Blender 2.90 addon that exports actions as separate fbx files for use in the [Stride3D Engine](https://github.com/stride3d/stride).

## Usage
Install the addon and select ```File > Export > Split and Export Animations```. It will export all actions that are saved using a fake user (have the little shield with a checkmark next to them) as individual fbx files in the same folder as your .blend file. The naming scheme is blendfilename_action.fbx. Import to Stride. Every fbx contains a single action, the mesh, and the skeleton.

You can also search for Split and Export Animations in the f3 menu.