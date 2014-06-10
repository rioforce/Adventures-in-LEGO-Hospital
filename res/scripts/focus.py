from bge import logic as g
from bge import render as r
from mathutils import *
from math import *
from bge import events
import bgl

cont = g.getCurrentController()
own = cont.owner
scene = g.getCurrentScene()
objects = scene.objects

focus = objects["focus"]
camera = scene.active_camera
keyboard = g.keyboard.events

def setFocus():  
	Ray = cont.sensors["Ray"]

	pos_vec = Vector(Ray.hitPosition)
	normal_vec = Vector(Ray.hitNormal)

	POP_OUT = 0.01

	focus.alignAxisToVect(-normal_vec.xyz, 2, 1)
	normal_vec.magnitude = POP_OUT

	focus.worldPosition = pos_vec + normal_vec

def getFocus():
	slowfocus = 0.94
	
	if not 'oldx' in own:
		own['oldx'] = 1.0
	if not 'oldy' in own:
		own['oldy'] = 1.0
	if not 'oldz' in own:
		own['oldz'] = 1.0

	#slow focusing
	own['oldx'] = (own['oldx']*slowfocus + focus.worldPosition[0]*(1-slowfocus))
	own['oldy'] = (own['oldy']*slowfocus + focus.worldPosition[1]*(1-slowfocus))
	own['oldz'] = (own['oldz']*slowfocus + focus.worldPosition[2]*(1-slowfocus))

	vecTo = Vector((own['oldx'],own['oldy'],own['oldz'])) - camera.worldPosition

	#z = camera.getDistanceTo(focus)
	z = vecTo.project(camera.getAxisVect((0.0, 0.0, 1.0))).magnitude
	own['focalDepth'] = z

def setLens():
	slowzoom = 0.9
	zoomin = events.UPARROWKEY
	zoomout = events.DOWNARROWKEY
	fstopminus = events.LEFTARROWKEY
	fstopplus = events.RIGHTARROWKEY


	if keyboard[zoomin]:
		own['focalLength'] += 1
	if keyboard[zoomout]:
		own['focalLength'] -= 1

	if keyboard[fstopplus]:
		own['stop'] += 1
	if keyboard[fstopminus]:
		own['stop'] -= 1

	if own['focalLength'] < 6:
		own['focalLength'] = 6

	elif own['focalLength'] > 600:
		own['focalLength'] = 600

	if own['stop'] < -1:
		own['stop'] = -1

	elif own['stop'] > 16:
		own['stop'] = 16

	FocalLength = own['focalLength']
	FocalDepth = own['focalDepth']

	f = FocalLength
	d = FocalDepth*1000 #mm to m

	own['fstop'] = round(pow(sqrt(2),own['stop']),1)
	

	hyperFocal = (f * f) / (own['fstop'] * 0.03)

	dofNear = (hyperFocal * d) / (hyperFocal + (d - f))

	dofFar = (hyperFocal * d) / (hyperFocal - (d - f))

	dofTotal = (dofFar - dofNear)

	own['hyperFocal'] = hyperFocal/1000
	own['dofNear'] = dofNear/1000
	own['dofFar'] = dofFar/1000
	own['dofTotal'] = dofTotal/1000

	if (camera.sphereInsideFrustum(focus.position, 0.1) != camera.OUTSIDE):
		FocalLength = max(FocalLength, 1.0/(1.0/FocalLength - 1.0/d))

	if not 'fLength' in own:
		own['fLength'] = camera.lens
	own['fLength'] = (own['fLength']*slowzoom + FocalLength*(1-slowzoom))

	camera.lens = own['fLength']