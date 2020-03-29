#!/usr/bin/env python

import pandas as pd
from datetime import datetime

# https://c19.se/Sweden/Västernorrland - Data for Västernorrland

START_DATE = '2020-03-02'
END_DATE = '2020-03-29'

TODAY = datetime.today().strftime('%Y-%m-%d')
OUTNAME = f'18_vasternorrland_{TODAY}.csv'

dates = pd.date_range(start=START_DATE, end=END_DATE)

confirmed = [
    0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 9, 11, 11, 11, 12, 13, 13, 14, 15, 15, 15, 15, 17, 19, 21, 25, 25, 25
]

fatalities = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

ICU = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 3, 3
]

sweden = pd.DataFrame(
    data = {'confirmed': confirmed,
            'fatalities': fatalities,
            'ICU': ICU},
    index = dates,
    dtype='Int64'
)

sweden.to_csv(f"data/{OUTNAME}", index=True, index_label='date')
