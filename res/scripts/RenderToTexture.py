######################################################
#
#    RenderToTexture.py        Blender 2.6
#
#    Tutorial for using RenderToTexture.py can be found at
#
#    www.tutorialsforblender3d.com
#
#    Released under the Creative Commons Attribution 3.0 Unported License.	
#
#    If you use this code, please include this information header.
#
######################################################

#import bge module
import bge

# get the current controller
controller = bge.logic.getCurrentController()
	
# get object script is attached to
obj = controller.owner

# check to see variable RenderToTexture has been created
if "RenderToTexture" in obj:
				
	# update the texture
	obj["RenderToTexture"].refresh(True)

# if variable RenderToTexture hasn't been created
else:
	
	## get current scene
	scene = bge.logic.getCurrentScene()
		
	# get a list of objects in the scene
	objList = scene.objects
	
	# get camera name being used for render to texture
	camName = obj['camera']
	
	# get camera object
	cam = objList[camName]
		
	# get the texture material ID
	matID = bge.texture.materialID(obj, "MA" + obj['material'])
	
	# set the texture
	renderToTexture = bge.texture.Texture(obj, matID)

	# get the texture image
	renderToTexture.source = bge.texture.ImageRender(scene,cam)

	# save RenderToTexture as an object variable
	obj["RenderToTexture"] = renderToTexture
	