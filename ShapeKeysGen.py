import bpy
objs = bpy.context.selected_objects

#will make a number of shape keys based on the items on this list
#the shape keys configured here are the ones used for VRchat facial animations
#but you can use all the ones you want (just don't remove the Basis one)

shapeName = ["Basis", "vrc.v_aa", "vrc.v_ch","vrc.v_dd","vrc.v_ee",
"vrc.v_ff","vrc.v_ih","vrc.v_kk","vrc.v_nn","vrc.v_oh","vrc.v_ou",
"vrc.v_pp","vrc.v_rr","vrc.v_sil","vrc.v_ss","vrc.v_th",
"vrc.blink_left","vrc.blink_right","vrc.lowerlid_left","vrc.lowerlid_right"]

#create the number of shape key
for i in range(len(shapeName)):
    bpy.ops.object.shape_key_add(from_mix=False)
# make a "list" of shape keys
selected_object = bpy.context.object
shape_keys = selected_object.data.shape_keys.key_blocks
#rename the shape keys
print("--------------------------------------")
i = 0
for obj in shape_keys:
    obj.name = shapeName[i]
    i+= 1
# to work the selected object have to have no shape key prior to this.
#if it does have it will make a mess. I could have added
# a function to check what number of shape keys it already have before
#but for my usecase it makes no sense. 
