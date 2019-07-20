from pyo import *

s = Server().boot()
s.start()
# mul is volume
mod = Sine(freq=6, mul=50)
mod2 = Sine(freq=6, mul=50)
b = Sine(freq=mod+mod2+440, mul=0.1).out()
s.gui(locals())
