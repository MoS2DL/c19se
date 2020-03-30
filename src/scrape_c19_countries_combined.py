#!/usr/bin/env python

from datetime import datetime
import os
import pandas as pd
import pathlib
import yaml

from utilities_c19_swedish_regions import (
    scrape_data_c19_sweden_region,
    create_dataframe,
    generate_csv
)


def main():
    with open('configuration/countries.yml') as f:
        configuration = yaml.load(f, Loader=yaml.FullLoader)

    now = datetime.now()
    date = f"{now.year}-{now.month:02d}-{now.day:02d}"
    NOW = f"{date}.{now.hour:02d}:{now.minute:02d}"

    outdir = pathlib.Path.cwd() / "data" / "scraped_c19" / "countries" / NOW
    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    countries = list(configuration.keys())
    dataframes = []  # Collect all, save region as column
    for country in countries:
        url = configuration[country]['url']
        file_prefix = configuration[country]['file_prefix']
        data = scrape_data_c19_sweden_region(url)

        dataframes.append(create_dataframe(data, country))

    df = pd.concat(dataframes)

    START_DATE = '2020-03-02'
    NOW = datetime.now()
    END_DATE = f"{NOW.year}-{NOW.month:02d}-{NOW.day:02d}"
    dates = pd.date_range(start=START_DATE, end=END_DATE)
    NOW = f"{END_DATE}.{NOW.hour:02d}:{NOW.minute:02d}"

    filename = f"c19se_all_countries_{NOW}.csv"
    filepath = outdir / filename

    df.to_csv(filepath, index=True, index_label='date')



if __name__ == "__main__":

    main()
