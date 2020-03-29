#!/usr/bin/env python

import pandas as pd

# https://c19.se/global -  Data for the world

START_DATE = '2020-03-02'
END_DATE = '2020-03-29'

dates = pd.date_range(start=START_DATE, end=END_DATE)

confirmed = [
    91011, 93555, 95843, 98596, 102551, 106571, 110544, 114330, 119363, 126643, 129209, 145977, 156888, 168248, 182373, 197940, 215720, 243511, 272982, 305349, 337901, 379391, 419537, 468442, 530427, 594080, 661509, 664717
]

fatalities = [
    3091, 3166, 3260, 3354, 3466, 3564, 3808, 3994, 4268, 4622, 4727, 5411, 5826, 6447, 7139, 7917, 8744, 9880, 11312, 12989, 14670, 16530, 18645, 21197, 23989, 27217, 31121, 31327
]

sweden = pd.DataFrame(
    data = {'confirmed': confirmed,
            'fatalities': fatalities,
            },
    index = dates,
    dtype='Int64'
)

sweden.to_csv('data/whole_world.csv', index=True, index_label='date')
