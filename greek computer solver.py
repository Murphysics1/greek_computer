import pandas as pd
import numpy as np
import gcf
import wheels

one = wheels.one
two = wheels.two

level1 = np.array([one[0],two[0]])
level2 = np.array([one[1],two[1]])

ring1 = gcf.ring(level1)
ring2 = gcf.ring(level2)

print(two)

two = np.roll(two,shift = 1, axis = 1)

print(two)


