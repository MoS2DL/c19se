#!/usr/bin/env python

import pandas as pd
from datetime import datetime

# https://c19.se/Sweden/Norrbotten - Data for Norrbotten

START_DATE = '2020-03-02'
END_DATE = '2020-03-29'

TODAY = datetime.today().strftime('%Y-%m-%d')
OUTNAME = f'15_norrbotten_{TODAY}.csv'

dates = pd.date_range(start=START_DATE, end=END_DATE)

confirmed = [
    0, 0, 0, 0, 0, 0, 0, 1, 2, 5, 6, 6, 8, 8, 8, 10, 10, 13, 17, 22, 22, 22, 25, 35, 40, 43, 43, 43
]

fatalities = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1
]

ICU = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 5, 10, 10, 10, 12, 14, 14
]

sweden = pd.DataFrame(
    data = {'confirmed': confirmed,
            'fatalities': fatalities,
            'ICU': ICU},
    index = dates,
    dtype='Int64'
)

sweden.to_csv(f"data/{OUTNAME}", index=True, index_label='date')
