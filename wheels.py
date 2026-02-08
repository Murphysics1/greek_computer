import numpy as np

e = np.nan
empty_row = [e, e, e, e, e, e, e, e, e, e, e, e]

one = np.array([[10, e, 7, e,15, e, 8, e, 3, e, 6, e],
                empty_row,
                empty_row,
                empty_row])

two = np.array([[11, 6,11, e, 6,17, 7, 3, e, 6, e,11],
                [14, e, 9, e,12, e, 4, e, 7,15, e, e],
                empty_row,
                empty_row])