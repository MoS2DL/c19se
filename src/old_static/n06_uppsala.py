#!/usr/bin/env python

import pandas as pd
from datetime import datetime

# https://c19.se/Sweden/Uppsala - Data for Uppsala

START_DATE = '2020-03-02'
END_DATE = '2020-03-29'

TODAY = datetime.today().strftime('%Y-%m-%d')
OUTNAME = f'06_uppsala_{TODAY}.csv'

dates = pd.date_range(start=START_DATE, end=END_DATE)

confirmed = [
    2, 2, 2, 4, 5, 5, 6, 8, 8, 11, 25, 25, 36, 38, 46, 46, 52, 67, 73, 74, 77, 82, 93, 102, 117, 129, 149, 149
]

fatalities = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 3, 3, 3, 3, 3, 3, 3
]

ICU = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 4, 5, 8, 9, 10, 10, 10
]

sweden = pd.DataFrame(
    data = {'confirmed': confirmed,
            'fatalities': fatalities,
            'ICU': ICU},
    index = dates,
    dtype='Int64'
)

sweden.to_csv(f"data/{OUTNAME}", index=True, index_label='date')
