#!/usr/bin/env python

import pandas as pd
from datetime import datetime

# https://c19.se/Sweden/Skåne - Data for Skåne

START_DATE = '2020-03-02'
END_DATE = '2020-03-29'

TODAY = datetime.today().strftime('%Y-%m-%d')
OUTNAME = f'03_skane_{TODAY}.csv'

dates = pd.date_range(start=START_DATE, end=END_DATE)

confirmed = [
    0, 1, 2, 9, 14, 17, 22, 22, 25, 60, 98, 129, 175, 197, 206, 209, 209, 216, 220, 223, 228, 231, 238, 246, 256, 264, 274, 276
]

fatalities = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 6, 7
]

ICU = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 6, 9, 9, 10, 11, 12, 15, 17
]

sweden = pd.DataFrame(
    data = {'confirmed': confirmed,
            'fatalities': fatalities,
            'ICU': ICU},
    index = dates,
    dtype='Int64'
)

sweden.to_csv(f"data/{OUTNAME}", index=True, index_label='date')
