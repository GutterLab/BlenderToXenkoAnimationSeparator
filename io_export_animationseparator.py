bl_info = {
        "name":         "Fbx Animation Splitter for Xenko",
        "category":     "Import-Export",
        "version":      (0,0,1),
        "blender":      (2,80,0),
        "location":     "File > Import-Export",
        "description":  "Split Animation Export",
        "category":     "Import-Export"
        }
        
import bpy
import os



def main(context):
#    print("test")
    startStates = []

    #record original state
    for i in range(0, len(bpy.data.actions)):
        print(str(i) + " " + str(bpy.data.actions[i]) + " " + str(bpy.data.actions[i].use_fake_user))
        startStates.append(bpy.data.actions[i].use_fake_user)
        bpy.data.actions[i].use_fake_user = False
    
    count = 0
    for i in range(0, len(bpy.data.actions)):
        if startStates[i]:
            bpy.data.actions[i].use_fake_user = True
            #export here
            blend_file_path = bpy.data.filepath
            directory = os.path.dirname(blend_file_path)
            #target_file = os.path.join(directory, bpy.path.basename(context.blend_data.filepath) + '_' + bpy.data.actions[i].name + '.fbx')
            target_file = os.path.join(directory, os.path.splitext(context.blend_data.filepath)[0] + '_' + bpy.data.actions[i].name + '.fbx')
            
            bpy.ops.export_scene.fbx(filepath = target_file, check_existing = True, object_types = {'ARMATURE'}, bake_anim_use_nla_strips = False, bake_anim_use_all_actions = False, bake_anim_force_startend_keyring = False)
            bpy.data.actions[i].use_fake_user = False
        
    #revert to what it was
    for i in range(0, len(bpy.data.actions)):
        bpy.data.actions[i].use_fake_user = startStates[i]

class SplitAnimations(bpy.types.Operator):
    """Split and Export Animations"""
    bl_idname = "object.splitanimations"
    bl_label = "Split and Export Animations"
    
    def execute(self, context):
        main(context)
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(operator.SplitAnimations.bl_idname, text="SplitAnimations")

def register():
    bpy.utils.register_class(SplitAnimations)
    
def unregister():
    bpy.utils.register_class(SplitAnimations)

if __name__ == "__main__":
    register()
