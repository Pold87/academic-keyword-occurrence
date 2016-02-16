# Historic word occurrence in academic papers

## Summary 

This script extracts the historic word occurrence of a search term in
academic papers (from Google Scholar). It allows for spotting trends
in research and analyzing the relevance of a topic over time.

## Usage

`python extract_occurrences.py '<keyword>' <start date> <end date>` 

This command lists the number of publications for every year using
this keyword. The script just searches for articles and excludes
patents and citations.

## Example

- Search term: 'bitcoin'
- Desired time span: 2000 to 2015
- Command: `python term_frequency.py 'bitcoin' 2000 2015` 
- Output: `out.csv`, with the following contents:
| year | results |
|------|---------|
| 2011 |    6320 |
| 2012 |    7250 |
| 2013 |    8170 |
| 2014 |    8260 |
| 2015 |    8150 |



 

