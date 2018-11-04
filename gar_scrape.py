"""GAR Scraper."""
import requests, csv, math
import datetime
from bs4 import BeautifulSoup

page = requests.get("http://www.gartran.com/main.php/current_loads?table_view=1&page_order=id&page_dir=xxx&page_num=1")
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find_all('tr')
test_date = datetime.datetime.strptime("01/01/2019", "%m/%d/%Y")
tomorrow = datetime.date.today() + datetime.timedelta(days=1)

all_trucks = []
all_miles = []
order_numbers = []
pick_dates = []
del_dates = []
origin_states = []
origin_cities = []
dest_states = []
dest_cities = []
miles = []

for i in range(1, len(table)):
    all_trucks.append(table[i].select('td')[8].get_text())

for i in range(1, len(table)):
    all_miles.append(table[i].select('td')[6].get_text())

for i in range(1, len(table)):
    if('V' in all_trucks[i-1]):
        order_numbers.append(table[i].select('td')[0].get_text())

for i in range(1, len(table)):
    del_date = table[i].select('td')[1].get_text()
    if('V' in all_trucks[i-1]):
        if(del_date == "ASAP"):
            pick_dates.append(datetime.datetime.strftime(tomorrow, "%m/%d/%Y"))
            del_dates.append(" ")
        else:
            travel = math.ceil(float(all_miles[i-1]) / 550)
            pick_date = datetime.datetime.strptime(del_date, "%m/%d/%Y") - datetime.timedelta(days=travel)
            pick_dates.append(datetime.datetime.strftime(pick_date, "%m/%d/%Y"))
            del_dates.append(del_date)

for i in range(1, len(table)):
    if('V' in all_trucks[i-1]):
        origin_states.append(table[i].select('td')[2].get_text())

for i in range(1, len(table)):
    if('V' in all_trucks[i-1]):
        origin_cities.append(table[i].select('td')[3].get_text())

for i in range(1, len(table)):
    if('V' in all_trucks[i-1]):
        dest_states.append(table[i].select('td')[4].get_text())

for i in range(1, len(table)):
    if('V' in all_trucks[i-1]):
        dest_cities.append(table[i].select('td')[5].get_text())

for i in range(1, len(table)):
    if('V' in all_trucks[i-1]):
        miles.append(table[i].select('td')[6].get_text())

with open('gar_data.csv', 'w', newline='') as gar_data:
    fieldnames = ['reference_id', 'origin_city', 'origin_state', 'origin_zip', 'destination_city', 'destination_state',
                    'destination_zip', 'truck_type', 'distance', 'pick_date', 'pick_time', 'drop_date', 'drop_time', 'stops',
                    'shipper']
    writer = csv.DictWriter(gar_data, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(0, len(order_numbers)):
        writer.writerow({'reference_id':order_numbers[i], 'origin_city':origin_cities[i], 'origin_state':origin_states[i],
                        'origin_zip':'', 'destination_city':dest_cities[i], 'destination_state': dest_states[i],
                        'destination_zip':'', 'truck_type': 'Dry Van', 'distance': miles[i], 'pick_date': pick_dates[i],
                        'pick_time': '', 'drop_date': del_dates[i], 'drop_time': '', 'stops': 0, 'shipper': 'GAR'
        })
