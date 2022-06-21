import click
from datetime import datetime
import pandas
from pathlib import Path
import time
import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
from plot_bar import plot_bar


@click.command()
@click.option("--search_term", prompt="Search term")
@click.option("--start_date", prompt="Start date", type=click.IntRange(1900, datetime.now().year))
@click.option("--end_date", prompt="End date", type=click.IntRange(1900, datetime.now().year))
def main(search_term, start_date, end_date):
    results_folder = Path(Path(__file__).parent.parent, "results")
    folder = Path(results_folder, f"{search_term.replace(' ', '-')}_{start_date}_{end_date}")
    if not folder.exists():
        folder.mkdir()
        print(f"Searchin results for {search_term} from {start_date} to {end_date}")
        years, results = find_results(search_term, start_date, end_date)
        df = pandas.DataFrame(data={"years": years, "results": results})
        df.to_csv(Path(folder, "results.csv"), sep=',', index=False)

        plot_bar(search_term, years, results)
        plt.savefig(Path(folder, "fig.png"), dpi=300)
    else:
        print(f"Results already exists in {folder}")


def find_results(search_term, start_date, end_date):
    years = list(range(start_date, end_date + 1))
    results = []

    for year in years:
        num_results, success = get_num_results(search_term, year)
        if not success:
            print("It seems that you made to many requests to Google Scholar. "
                  "Please wait a couple of hours and try again.")
            exit(-1)
        results.append(num_results)
        print(f"{year}, {num_results}")
        time.sleep(2)

    return years, results


def get_num_results(search_term, year):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        'referer': 'https://scholar.google.com/'
    }
    url = f"""https://scholar.google.com/scholar?q={search_term}&hl=en&as_ylo={year}&as_yhi={year}"""
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        html = response.content

        # Create soup for parsing HTML and extracting the relevant information
        soup = BeautifulSoup(html, 'html.parser')
        div_results = soup.find("div", {"id": "gs_ab_md"})  # find line 'About x results (y sec)

        if div_results is not None:
            res = re.findall(r'(\d+).?(\d+)?.?(\d+)?\s', div_results.text)  # extract number of search results
            if len(res) > 0:
                num_results = int(''.join(res[0]))  # convert string to number
                return num_results, True

    return 0, False


if __name__ == '__main__':
    main()
