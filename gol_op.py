import bpy
from bpy.types import Operator
import random
from . gol_funcs import *

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
            bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value":(random.randint(-10,10), random.randint(-10, 10), random.randint(-10, 10))})

class GOL_OT_Stop(Operator):
    bl_idname = "gol.stop"
    bl_label = "Stop Generator"
    bl_description = "Stop Generating Iterations"
     
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
        # Delete all selected objects
        bpy.ops.object.delete()

class GOL_OT_Spawn(Operator):
    bl_idname = "gol.spawn"
    bl_label = "Fill Grid"
    bl_description = "Fill Grid with Objects"

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == "OBJECT":
                return True
        
        return False
    
    def execute(self, context):
        # Generate a 2D array 
        grid = generate_grid(10)

        # Delete 20 random items from grid 
        b = delete_random_item(grid, 50)
        
        # Add new object to grid locations
        for i in range(0,len(b)):
            bpy.ops.object.duplicate()
            bpy.context.object.location =(b[i][0], b[i][1], b[i][2])               

        # Generate 

