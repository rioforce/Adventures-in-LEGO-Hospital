"""Screenshot script"""

import bge
import time
import os

# (Possible) cross-platform location of user's Pictures folder
pictures_folder = os.path.join(os.path.expanduser("~"), "Pictures")

# Location of Screenshots folder in user's Pictures folder
screens = os.path.join(pictures_folder, "Adventures in LEGO Hospital")
 
# Create folder if it does not exist 
if not os.path.exists(screens): os.mkdir(screens)

# Save image in Adventures in LEGO Hospital folder, use current date and time
bge.render.makeScreenshot(os.path.join(screens, "LEGO-Hospital_{0}.png".format(time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()))))