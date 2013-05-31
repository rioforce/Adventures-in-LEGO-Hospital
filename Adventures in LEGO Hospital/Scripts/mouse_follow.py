import Rasterizer

g = GameLogic
c = g.getCurrentController()
o = c.getOwner()

mMove = c.getSensor("Move")

width = float(Rasterizer.getWindowWidth())
height = float(Rasterizer.getWindowHeight())

aspecty = height/12.0
aspectx = width/16.0

o.MouseX = (mMove.getXPosition()-width/2)/aspectx
o.MouseY = -(mMove.getYPosition()-height/2)/aspecty

o.setPosition([o.MouseX + 0.2,o.MouseY - 0.3,0]) 


# Script from http://www.blender.org/forum/viewtopic.php?t=352&sid=7f358240b210dc5a74e3e959f254c6f9