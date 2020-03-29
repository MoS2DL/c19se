#!/usr/bin/env python

import pandas as pd
from datetime import datetime

# https://c19.se/Sweden/Stockholm - Data for Stockholm

START_DATE = '2020-03-02'
END_DATE = '2020-03-29'

TODAY = datetime.today().strftime('%Y-%m-%d')
OUTNAME = f'01_stockholm_{TODAY}.csv'

dates = pd.date_range(start=START_DATE, end=END_DATE)

confirmed = [
    5, 15, 31, 59, 80, 102, 114, 146, 207, 233, 267, 308, 341, 359, 377, 410, 446, 501, 606, 661, 760, 816, 959, 1070, 1216, 1311, 1538, 1538
]

fatalities = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 5, 5, 5, 5, 8, 10, 10, 16, 19, 37, 43, 60, 63, 63
]

ICU = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 42, 47, 62, 80, 95, 107, 117, 129, 140
]

sweden = pd.DataFrame(
    data = {'confirmed': confirmed,
            'fatalities': fatalities,
            'ICU': ICU},
    index = dates,
    dtype='Int64'
)

sweden.to_csv(f"data/{OUTNAME}", index=True, index_label='date')
