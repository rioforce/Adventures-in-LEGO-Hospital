""" 
Toggle between Fullscreen and Windowed mode
Written by Triangle717
<http://Triangle717.WordPress.com/>
"""

"""The Issues:
* Once either block is finished, it promptly runs the other block, thus not performing the desired actiom
* I can get it to work only while the hotkey is held-down, not the way it needs to be
* When fullscreen is activated, it loads in 1080p (as it is says below), but it needs to open in the screen's current resolution.
However, I can't use bpy.types.SceneGameData.use_desktop as the bpy module is not compiled into a standalone runtime, and there is no
bge.render version of it (though there should be).
"""
    
import bge

def main():
    if bge.render.getFullScreen():
        windowed()
    elif not bge.render.getFullScreen(): 
        fullscreen()
    

# It is full screen, kick to windowed mode
def windowed():
    bge.render.setFullScreen(False)
    bge.render.setWindowSize(960, 540)
    #raise SystemExit

# It is windowed mode, kick to full screen 
def fullscreen(): 
    bge.render.setFullScreen(True)
#    bge.render.setWindowSize(1920, 1080)   
    #raise SystemExit
    
main()