import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get("http://www.gartran.com/main.php/current_loads?table_view=1&page_order=id&page_dir=xxx&page_num=1")
soup = BeautifulSoup(page.content, 'html.parser')

truck_types = []
order_numbers = []
del_dates = []
origin_states = []
origin_cities = []
dest_states = []
dest_cities = []
miles = []

for i in range(1, len(table)):
    if('V' in truck_types[i-1]):
        origin_states.append(table[i].select('td')[2].get_text())

for i in range(1, len(table)):
    if('V' in truck_types[i-1]):
        origin_cities.append(table[i].select('td')[3].get_text())

for i in range(1, len(table)):
    if('V' in truck_types[i-1]):
        dest_states.append(table[i].select('td')[4].get_text())

for i in range(1, len(table)):
    if('V' in truck_types[i-1]):
        dest_cities.append(table[i].select('td')[5].get_text())

for i in range(1, len(table)):
    if('V' in truck_types[i-1]):
        miles.append(table[i].select('td')[6].get_text())
