#!/usr/bin/env python

from datetime import datetime
import os
import pandas as pd
import pathlib
import yaml

from utilities_c19_swedish_regions import (
    scrape_data_c19_sweden_region,
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

    regions = list(configuration.keys())
    for region in regions:
        url = configuration[region]['url']
        file_prefix = configuration[region]['file_prefix']
        data = scrape_data_c19_sweden_region(url)

        generate_csv(data, file_prefix, outdir)


if __name__ == "__main__":

    main()
