from pyo import *

s = Server().boot()
s.start()
# mul is volume
a = Sine(mul=0.01).out() # Defaults to frequency of 1000
b = Sine(freq=700, mul=0.01).out()
s.gui(locals())
