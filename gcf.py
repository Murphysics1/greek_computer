import numpy as np
import wheels

def ring(level):

    r = []
    level_t = level.T

    for row in level_t:
        mask = np.isfinite(row)
        row = row[mask]
        if row.size > 0:
            r.append(row[0])
        else:
            r.append(np.nan)
    
    return np.array(r)

def level(idx):

    arr = [wheels.one[idx],
           wheels.two[idx],
           wheels.three[idx],
           wheels.four[idx],
           wheels.five[idx]]

    return np.array(arr)