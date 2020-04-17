from bs4 import BeautifulSoup
import pdb
import requests
import json

url = "https://animalcrossing.fandom.com/wiki/Bugs_(New_Horizons)"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
#print(soup.prettify()) # print the parsed data of html

# need to look at source code on page to get specific tables
# first is northern, last is southern
bugs_tables = soup.find_all("table", attrs={"style": "margin: 0 auto; width: 100%; background:#92B05A; text-align:center; solid #92B05A; border-radius: 20px; -moz-border-radius: 20px; -webkit-border-radius: 20px; -khtml-border-radius: 20px; -icab-border-radius: 20px; -o-border-radius: 20px;"})

nothern_bugs_table = bugs_tables[0]
southern_bugs_table = bugs_tables[1]

n_bugs_data = nothern_bugs_table.find_all("tr")
s_bugs_data = southern_bugs_table.find_all("tr")

# HELPER FUNCTIONS
def text_cleaner(text):
  return text.replace('\n', '').strip()

# Create an array of col titles to use in loop for creating bug_data dicts
bugs_col_titles = []
for title in nothern_bugs_table.find_all("th"):
   bugs_col_titles.append(text_cleaner(title.text).lower())


# Create Lists
def create_bug_dict(bug_row):
  bug_data = bug_row.find_all("td")
  curr_bug = {}
  i = 0
  while i < len(bug_data):
    if i == 1:
      img_path = bug_data[i].find("img")
      curr_bug[bugs_col_titles[i]] = img_path["data-src"]
    else:
      curr_bug[bugs_col_titles[i]] = text_cleaner(bug_data[i].text.lower())
    i += 1
  return curr_bug

def create_bug_list(raw_bugs_list):
  i = 0
  bugs_list = []
  
  while i < len(raw_bugs_list):
    if i != 0:
      bugs_list.append(create_bug_dict(raw_bugs_list[i]))
    i += 1
  return bugs_list
    
#Create JSON

bug_json = {
  'northern': create_bug_list(n_bugs_data),
  'southern': create_bug_list(s_bugs_data)
}

with open('bugs.json', 'w') as json_file:
  json.dump(bug_json, json_file)
