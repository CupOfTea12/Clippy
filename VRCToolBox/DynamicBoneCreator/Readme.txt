To add the bones to the list, you can follow these steps:

1.Create a new empty game object in your scene and name it "DynamicBoneCreator".

2.Attach the "DynamicBoneCreator" script to the game object.

3.Drag and drop the game object that you want to attach dynamic bones to into the "targetObject" field in the "DynamicBoneCreator" script.

4.In the Unity editor, select the game object that you want to attach dynamic bones to.

5.In the inspector, expand the game object's hierarchy and find the bones that you want to attach dynamic bones to. For example, if you want to attach dynamic bones to the "Tail_Rt" bone, find the "Tail_Rt" bone in the hierarchy.

6.Click on the bone to select it.

7.In the "DynamicBoneCreator" script, click on the "Add Element" button in the "Bones To Attach" field.

8.Drag and drop the bone you want to apply the dynamic script on from the hierarchy into the new element that you just added.

9.Repeat steps 6 to 8 for all the bones that you want to attach dynamic bones to.

10.Modify the damping, elasticity, stiffness, and inert values in the "DynamicBoneCreator" script as per your requirements.

11.Play the scene to test the dynamic bones.

Once you've added the bones to the list, the script will automatically attach dynamic bones to those bones with the specified settings when you play the scene.
