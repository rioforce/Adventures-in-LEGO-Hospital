""" 
Toggle between Fullscreen and Windowed mode
Written by Triangle717
<http://Triangle717.WordPress.com/>
"""

import bge
try:
    import bpy
except ImportError:
    bpy = None

if bge.render.getFullScreen():
    bge.render.setWindowSize(640, 480)
    SceneGameData.use_desktop = False
    #bpy.context.scene.game_settings.use_desktop = False
    bpy.context.scene.game_settings.show_fullscreen = False

elif not bge.render.getFullScreen():
    bpy.context.scene.game_settings.use_desktop = True
    bge.render.setWindowSize(1920, 1080)
    bpy.context.scene.game_settings.show_fullscreen = True




