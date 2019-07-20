from pyo import *
import time

s = Server().boot()
s.start()
# mul is volume
mod = Sine(freq=6, mul=50)
mod2 = Sine(freq=6, mul=50)
b = Sine(freq=mod+mod2+440, mul=0.1).out()
time.sleep(3)
mod2.freq = 3
time.sleep(3)
mod2.freq = 2
time.sleep(3)
mod2.freq = 1
time.sleep(3)
mod2.mul = 200
time.sleep(3)
