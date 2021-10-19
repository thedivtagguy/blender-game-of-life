import bpy
from bpy.types import Operator
import random

class GOL_OT_Start(Operator):
    bl_idname = "gol.start"
    bl_label = "Start Generator"
    bl_description = "Start Generating Iterations"
     
    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == "OBJECT":
                return True
        
        return False

    def execute(self, context):
        
        # Get active object
        active_obj = context.view_layer.objects.active
        for i in range(0,5):
        # Duplicate active object to new location
            bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value":(random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))})