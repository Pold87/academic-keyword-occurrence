# Occurrence of a list of keywords in google academic. Extraction of search results.

## Summary

This script extracts the number of results from a list of search terms in academia (from Google Scholar). It helps to prioritise research niches and where there may be under-researched needs.

It can be useful when focusing a scientific review to see where the most information is to be found.

There is a Python 3 branch (master) and a Python 2 branch (python2).

## Usage

Add the list of keywords you want to search for in `input.csv` and run the script. If you want to search for combinations of words, add a + between them.

`python extract_occurrences.py`

The script just searches for articles and excludes
patents and citations.

**visualization.ipynb**: This notebook helps to visualise the scraping results by generating a bar chart.

### Alternative: Usage with Docker

You can use [Docker](https://www.docker.com/) to run this script, without the need of having Python or its dependencies installed.

1. Update the `command` with your search term and time range in `docker-compose.yml`
2. run `docker-compose up`

## Example

- Search terms: 'sarcopenia + {drugs for cancer treatment}'
- Command: `python extract_occurrences.py`
- Output: `out.csv`, with the following contents:

| search_term | results |
|------|---------
| ...  |    ...  |	|
| sarcopenia+PEMBROlizumab |    1340  |
| sarcopenia+OSIMERTINIB   |    179   |
| sarcopenia+NIVOlumab     |    1490  |
| sarcopenia+ABEMACICLIB   |    77    |
| sarcopenia+PERTuzumab    |    208   |

![sarcopenia and drugs chart](https://github.com/BreisOne/academic-keyword-occurrence/blob/master/bar_plot_results.jpg "sarcopenia and drugs chart")

## Credits
Created by Volker Strobel - volker.strobel87@gmail.com
adapted by Brais Bea - b.mascat@gmail.com

If you use this code in academic papers, please cite this repository via Zenodo (http://doi.org/10.5281/zenodo.1218409):

Volker Strobel. (2018, April 14). Pold87/academic-keyword-occurrence: First release (Version v1.0.0). Zenodo. http://doi.org/10.5281/zenodo.1218409
