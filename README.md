# Historic word occurrence in academic papers

## Summary

This script extracts the historic word occurrence of a search term in
academic papers (from Google Scholar). It allows for spotting trends
in research and analyzing the relevance of a topic over time.

There is a Python 3 branch (master) and a Python 2 branch (python2).

## Usage

### Command line arguments

`python extract_occurrences.py '<keyword>' <start date> <end date>`

This command lists the number of publications for every year using
this keyword. The script just searches for articles and excludes
patents and citations.

### User input

If no argument are given as input, the user can use the prompt to enter the needed information.

```
> Search term: <keyword>
> Start date: <start date>
> End date: <end date>
```

## Usage with Docker-Compose

You can use [Docker](https://www.docker.com/) to run this script, without the need of having Python or its dependencies installed.

1. Update the `command` with your search term and time range in `docker-compose.yml`
2. run `docker-compose up`

## Example

- Search term: 'bitcoin'
- Desired time span: 2000 to 2015
- Command: `python extract_occurrences.py 'bitcoin' 2005 2010`
- Output: A new folder is created in `results` folder with the following contents:
    - `results.csv` file
    - `fig.png` file

### Content example
| year | results |
|------|---------|
| ...  |    ...  |
| 2011 |    141  |
| 2012 |    292  |
| 2013 |    889  |
| 2014 |    2370 |
| 2015 |    2580 |


![bitcoin chart](https://raw.githubusercontent.com/Pold87/academic-keyword-occurrence/master/bitcoin_chart.png "bitcoin chart")

## Credits
Created by Volker Strobel - volker.strobel87@gmail.com

If you use this code in academic papers, please cite this repository via Zenodo (http://doi.org/10.5281/zenodo.1218409):

Volker Strobel. (2018, April 14). Pold87/academic-keyword-occurrence: First release (Version v1.0.0). Zenodo. http://doi.org/10.5281/zenodo.1218409

### Contributors
Patrick Hofmann
Cédric Gilon


