import bs4 as bs
import urllib.request
import pandas as pd

site_byte = urllib.request.urlopen('https://en.wikipedia.org/wiki/List_of_United_States_counties_and_county_equivalents').read()

# Takes the site bytes and turns them into a bs4.BeautifulSoup object, which looks like html,
# and reads like it if the .prettify() method is applied.

soup = bs.BeautifulSoup(site_byte, 'lxml')

table_byte = soup.find("table")

table_soup = bs.BeautifulSoup(str(table_byte), 'lxml')

html_heads = table_byte.find_all('th')

dummy_headers = [html_heads[i].text.strip() for i in range(len(html_heads))]

headers = [i.replace('\xa0', ' ') for i in dummy_headers]

headers.append('Link')
# result: ['INCITS', 'County or equivalent', 'State, district or territory', '2013 Pop', 'Core Based Statistical Area', 'Combined Statistical Area', 'Link']

html_rows = table_byte.find_all('td')

links = [html_rows[i].a for i in range(len(html_rows))]


def chunks(lst, n):
    for z in range(0, len(lst), n):
        yield lst[z:z + n]


link_chunks = list(chunks(links, 6))

county_stuff = [i[1] for i in link_chunks]

samples = county_stuff[0:1]

sample = samples[0]

sample.get('href')

jus_links = [it.get('href') for it in county_stuff]

bodies = [html_rows[i].text.strip() for i in range(len(html_rows))]

split_data = list(chunks(bodies, 6))

for i in range(len(jus_links)):
    split_data[i].append(jus_links[i])

wiki_counties = pd.DataFrame(split_data, columns=headers)

just = 'checking'

