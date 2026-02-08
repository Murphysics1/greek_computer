import pandas as pd
import numpy as np
import gcf
import wheels

one   = wheels.one
two   = wheels.two
three = wheels.three
four  = wheels.four
five  = wheels.five

levels = []
rings = []

for idx in range(1,5):
    levels.append(gcf.level(idx))

for r in range(1,5):
    rings.append(gcf.ring(levels[r-1]))

rings = np.array(rings)

print(rings)
