# BlenderToXenkoAnimationSeparator
A blender 2.8 script that exports actions as separate fbx files for use in Xenko.

## Usage
Install the addon and push f3 (windows default) to open the search. Type in Split Animation Export and select it. It will export all actions that are saved using a fake user (have the little F next to them) as individual fbx files in the same folder as your .blend file. The naming scheme is blendfilename_action.fbx. Import to xenko. Every fbx contains a single action, the mesh, and the skeleton.