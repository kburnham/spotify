


# script to scrape https://schedule.sxsw.com/2024/artists and get a list of all the artists
import pandas as pd
from bs4 import BeautifulSoup
import requests
import pickle

url = 'https://schedule.sxsw.com/2024/artists'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
# table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="pbp") 



links = soup.find_all('a', {'class': ['link-primary']})

for link in links:
    if link.find(class_ = 'link-primary card-link'):
        print(link.text)
    

all_artists = list()
for a in links:
    if 'genre' not in a['href']:
        all_artists.append(a.text)


len(all_artists)


with open('/Users/kevin/spotify/artist_lists/sxsw_2024_artists.txt', 'w') as outfile:
  outfile.write('\n'.join(str(i) for i in all_artists))
