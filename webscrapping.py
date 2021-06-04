import requests
from bs4 import BeautifulSoup
import pandas as pd


page = requests.get("https://www.imdb.com/list/ls091520106/?st_dt=&mode=detail&page=1&sort=list_order,asc")

soup = BeautifulSoup(page.content, 'html.parser')

all_data = soup.find_all('div', class_ = "lister-item-content")

print(all_data)

# lists for storage
movie_name = []
desc = []
release_date = []
director = []
rating = []
duration = []
genre = []
actors = []
filming_dates = []


######## Fill lists with extracted data ########

#Movie Name
#name_all = all_data.find_all('h3', class_ = 'lister-item-header')

for data in all_data:
    name_text = name.find('a').text
    movie_name.append(name_text)


print(movie_name)


#Description
#desc_all = soup.find_all('div', class_= "lister-item-content")



#print(desc_all)
