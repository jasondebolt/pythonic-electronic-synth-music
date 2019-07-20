from pyo import *

s = Server().boot()
s.start()
a = Sine(freq=1000, phase=0, mul=0.01, add=0).out()
s.gui(locals())
