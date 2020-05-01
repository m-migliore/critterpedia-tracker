from bs4 import BeautifulSoup
import pdb
import requests
import json

url = "https://animalcrossing.fandom.com/wiki/Fish_(New_Horizons)"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
#print(soup.prettify()) # print the parsed data of html

# need to look at source code on page to get specific tables
# first is northern, last is southern
fish_tables = soup.find_all("table", attrs={"style": "width:100%; background:#76acda; text-align:center;"})
nothern_fish_table = fish_tables[0]
southern_fish_table  =fish_tables[1]

n_fish_data = nothern_fish_table.find_all("tr")
s_fish_data = southern_fish_table.find_all("tr")

# HELPER FUNCTIONS
def text_cleaner(text):
  return text.replace('\n', '').strip()

# Create an array of col titles to use in loop for creating fish_data dicts
fish_col_titles = []
for title in nothern_fish_table.find_all("th"):
   fish_col_titles.append(text_cleaner(title.text).lower())


# Create Lists
def create_fish_dict(fish_row):
  fish_data = fish_row.find_all("td")
  curr_fish = {}
  i = 0
  while i < len(fish_data):
    # fish_data[1] is the image path
    if i == 1:
      img_path = fish_data[i].find("img")
      curr_fish[fish_col_titles[i]] = img_path["data-src"]
    elif i > 5:
      # fish_data[> 5] are the active months 
      curr_fish[fish_col_titles[i]] = text_cleaner(fish_data[i].text.title()) == "\u2713"
    else:
      curr_fish[fish_col_titles[i]] = text_cleaner(fish_data[i].text.title())
    i += 1
  return curr_fish

def create_fish_list(raw_fish_list):
  i = 0
  fish_list = []

  while i < len(raw_fish_list):
    if i != 0:
      fish_list.append(create_fish_dict(raw_fish_list[i]))
    i += 1
  return fish_list
    
#Create JSON

fish_json = {
  'northern': create_fish_list(n_fish_data),
  'southern': create_fish_list(s_fish_data)
}

with open('./fish.json', 'w') as json_file:
  json.dump(fish_json, json_file)
