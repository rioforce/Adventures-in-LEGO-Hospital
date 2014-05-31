co = bge.logic.getCurrentController()
lamp = co.owner
toggle = co.sensors["shadow-toggle"] # space is the name of keyboard sensor

if toggle.positive:
    lamp.energy = 0.3 - lamp.energy