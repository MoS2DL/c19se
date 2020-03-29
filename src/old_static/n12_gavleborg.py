#!/usr/bin/env python

import pandas as pd
from datetime import datetime

# https://c19.se/Sweden/Gävleborg - Data for Gävleborg

START_DATE = '2020-03-02'
END_DATE = '2020-03-29'

TODAY = datetime.today().strftime('%Y-%m-%d')
OUTNAME = f'12_gavleborg_{TODAY}.csv'

dates = pd.date_range(start=START_DATE, end=END_DATE)

confirmed = [
    0, 0, 0, 1, 2, 2, 2, 2, 2, 3, 5, 5, 6, 7, 8, 9, 13, 15, 17, 20, 24, 24, 27, 32, 39, 44, 53, 53
]

fatalities = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1
]

ICU = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 4, 5, 5, 5, 5
]

sweden = pd.DataFrame(
    data = {'confirmed': confirmed,
            'fatalities': fatalities,
            'ICU': ICU},
    index = dates,
    dtype='Int64'
)

sweden.to_csv(f"data/{OUTNAME}", index=True, index_label='date')
