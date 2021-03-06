#!/usr/bin/env python

from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import pathlib
import requests


START_DATE = '2020-03-02'
NOW = datetime.now()
END_DATE = f"{NOW.year}-{NOW.month:02d}-{NOW.day:02d}"


def scrape_data_c19_sweden_region(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    scripts = soup.find_all("script")
    script = scripts[-1]

    script_split_newline = script.text.split('\n')
    data_list = []
    for line in script_split_newline:
        if 'data' in line:
            try:
                data = [int(x) for x in line[7:-1].split(',')]
                data_list.append(data)
            except ValueError:
                continue

    data = {
        'confirmed': data_list[0],
        'fatalities': data_list[2],
        'ICU': data_list[3]
    }

    return data


def create_dataframe(data, name):
    dates = pd.date_range(start=START_DATE, end=END_DATE)
    df = pd.DataFrame(
        data=data,
        index=dates,
        dtype='Int64'
    )

    df['region'] = name

    return df


def generate_csv(data, file_prefix, outdir, name=None):

    dates = pd.date_range(start=START_DATE, end=END_DATE)
    NOW = f"{END_DATE}.{NOW.hour:02d}:{NOW.minute:02d}"
    filename = f"{file_prefix}_{NOW}.csv"
    filepath = outdir / filename

    df = pd.DataFrame(
        data=data,
        index=dates,
        dtype='Int64'
    )

    if name:
        df['region'] = name

    df.to_csv(filepath, index=True, index_label='date')


if __name__ == "__main__":

    url = 'https://c19.se/Sweden/Stockholm'
    print(scrape_data_c19_sweden_region(url))
