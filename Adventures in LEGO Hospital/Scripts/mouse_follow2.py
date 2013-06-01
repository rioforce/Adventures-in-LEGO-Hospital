from bge import logic as g, render as r

c = g.getCurrentController()
o = c.owner

m = c.sensors["Mouse"]

p = o.parent

w1 = r.getWindowHeight()
w2 = r.getWindowWidth()

h1 = w1//2
h2 = w2//2

s = 0.005

x, y = m.position

x = (h1 - x)*s
y = (h2 - y)*s

o.applyRotation([y,0.0,0.0],True)
p.applyRotation([0.0,0.0,x],False)

r.setMousePosition(h1, h2)