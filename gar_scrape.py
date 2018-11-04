import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get("http://www.gartran.com/main.php/current_loads?table_view=1&page_order=id&page_dir=xxx&page_num=1")
soup = BeautifulSoup(page.content, 'html.parser')

truck_types = []
origin_states = []
origin_cities = []
dest_states = []
dest_cities = []
miles = []
