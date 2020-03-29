# c19se

Collection of scripts for scraping Swedish region data from c19.se.

The scraping writes to a directory under `data/scraped_c19` named with the date and time at scraping.

The urls are defined in a the yaml-file `configuration/swedish_regions.yml`.


### Usage

Just run the `src/scrape_c19_swedish_regions.py` script from the root directory.

### External dependencies

The code utilizes the following external dependencies

1. Beautiful soup 4 (`pip install beautifulsoup4` or `conda install -c conda-forge beautifulsoup4`)
2. requests (`pip install requests` or `conda install -c conda-forge requests`)
3. PyYAML (`pip install pyyaml` or `conda install -c conda-forge pyyaml` )
4. Pandas (`pip install pandas` or `conda install -c conda-forge pandas`)
