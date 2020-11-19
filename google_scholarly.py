"""
Script to get h-index, i-index, and recent publications for desired researchers.
"""

# !pip install scholarly

from scholarly import scholarly
import csv

fname = 'google_scholar_data.csv'

author_names = ['Brian MacVicar', 'Jeffrey LeDue', 'Tim H. Murphy'] # Edit this to get data on other researchers
query_row = ['Name', 'H Index', 'H Index 5 years', 'I Index', 'I Index 5 years', 'Pub 1','Pub 2','Pub 3']

with open(fname, mode='w') as csv_file:
  csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  csv_writer.writerow(query_row)

  for author_string in author_names:
    search_query = scholarly.search_author(author_string)
    author = next(search_query).fill()

    hindex = author.hindex
    hindex5 = author.hindex5y
    i10index = author.i10index
    i10index5 = author.i10index5y

    publications = author.publications
    new_publications = [pub for pub in publications if 'year' in pub.bib.keys()]
    sorted_pubs = sorted(new_publications,key=lambda pub : pub.bib['year'], reverse=True)
    recent_pubs = [pub.bib['title'] for pub in sorted_pubs[0:3]]

    row = [author_string,hindex,hindex5,i10index,i10index5] + recent_pubs
    csv_writer.writerow(row)

