import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get("http://www.gartran.com/main.php/current_loads?table_view=1&page_order=id&page_dir=xxx&page_num=1")
soup = BeautifulSoup(page.content, 'html.parser')

order_numbers = [order.get_text() for order in soup.find_all(class_="tablelink")]
print(order_numbers)
