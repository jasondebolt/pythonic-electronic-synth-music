from pyo import Server, Sine, LFO
from pesm import Keys, ThreeKeys

s = Server().boot()
all_waves = []

def e_minor_heartbeat():
  mul = 0.05
  ind = LFO(freq=1, type=1, mul=.5, add=.5)
  for _key in ThreeKeys:
      kwargs = {'freq': _key.freq, 'mul': mul}
      if _key == Keys.E2:
          kwargs['mul'] = mul*ind*10
      all_waves.append(Sine(**kwargs).out())

e_minor_heartbeat()
s.gui(locals())
