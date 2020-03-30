#!/usr/bin/env python

import pandas as pd
from datetime import datetime

# https://c19.se/Sweden/Stockholm - Data for Stockholm

START_DATE = '2020-03-02'
END_DATE = '2020-03-29'

TODAY = datetime.today().strftime('%Y-%m-%d')
OUTNAME = f'02_vastra_gotaland_{TODAY}.csv'

dates = pd.date_range(start=START_DATE, end=END_DATE)

confirmed = [
    6, 9, 11, 12, 14, 14, 26, 33, 48, 85, 116, 134, 155, 159, 176, 179, 199, 207, 228, 242, 250, 254, 265, 275, 297, 317, 330, 330
]

fatalities = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 4, 4, 4
]

ICU = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 23, 25, 30, 34, 39, 41, 41
]

sweden = pd.DataFrame(
    data = {'confirmed': confirmed,
            'fatalities': fatalities,
            'ICU': ICU},
    index = dates,
    dtype='Int64'
)

sweden.to_csv(f"data/{OUTNAME}", index=True, index_label='date')
