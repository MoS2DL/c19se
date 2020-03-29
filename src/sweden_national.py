#!/usr/bin/env python

import pandas as pd

# https://c19.se - Landing page - Data for Sweden

START_DATE = '2020-03-02'
END_DATE = '2020-03-29'
OUTNAME = '00_sweden_national.csv'

dates = pd.date_range(start=START_DATE, end=END_DATE)

confirmed = [
    15, 30, 52, 94, 137, 162, 203, 260, 356, 500, 687, 812, 967, 1032, 1121, 1196, 1295, 1443, 1650, 1784, 1929, 2059, 2299, 2527, 2855, 3069, 3460, 3478
]

fatalities = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 3, 7, 8, 10, 11, 16, 20, 23, 33, 40, 63, 78, 105, 112, 116
]

ICU = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 77, 91, 137, 177, 219, 255, 287, 313, 331
]

sweden = pd.DataFrame(
    data = {'confirmed': confirmed,
            'fatalities': fatalities,
            'ICU': ICU},
    index = dates,
    dtype='Int64'
)

sweden.to_csv(f"data/{OUTNAME}", index=True, index_label='date')
