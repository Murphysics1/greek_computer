import pandas as pd
import numpy as np

e = np.nan
empty_row = [e, e, e, e, e, e, e, e, e, e, e, e]

wheel_1 = np.array([[10, e, 7, e,15, e, 8, e, 3, e, 6, e],
                  empty_row,
                  empty_row,
                  empty_row])

wheel_2 = np.array([[11, 6,11, e, 6,17, 7, 3, e, 6, e,11],
                    [14, e, 9, e,12, e, 4, e, 7,15, e, e],
                    empty_row,
                    empty_row])

level = np.array([wheel_1[0],wheel_2[0]])

def ring(level):

    r = []
    level_t = level.T

    for row in level_t:
        mask = np.isfinite(row)
        row = row[mask]
        if row.size > 0:
            r.append(row[0])
        else:
            r.append(e)
    
    return np.array(r)

ring1 = ring(level)

print(ring1)

