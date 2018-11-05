"""GAR Scraper."""
import csv, datetime, math, requests, sys
from bs4 import BeautifulSoup

def get_data():
    column = [order_numbers, drop_dates, origin_states, origin_cities, dest_states, dest_cities, miles]
    for i in range(1, len(table)):
        if('V' in all_trucks[i-1]):
            for j in range(0, len(column)):
                if(j == 1):
                    drop_date = table[i].select('td')[1].get_text()
                    if(drop_date == "ASAP"):
                        pick_dates.append(datetime.datetime.strftime(tomorrow, "%m/%d/%Y"))
                        drop_dates.append(" ")
                    else:
                        travel = math.ceil(float(all_miles[i-1]) / 550)
                        pick_date = datetime.datetime.strptime(drop_date, "%m/%d/%Y") - datetime.timedelta(days=travel)
                        pick_dates.append(datetime.datetime.strftime(pick_date, "%m/%d/%Y"))
                        drop_dates.append(drop_date)
                else:
                    column[j].append(table[i].select('td')[j].get_text())

def write_csv():
    with open(csv_name, 'w', newline='') as gar_data:
        writer = csv.DictWriter(gar_data, fieldnames=['reference_id', 'origin_city', 'origin_state', 'origin_zip',
                                                      'destination_city', 'destination_state', 'destination_zip',
                                                      'truck_type', 'distance', 'pick_date', 'pick_time', 'drop_date',
                                                      'drop_time', 'stops', 'shipper'])
        
        writer.writeheader()
        for i in range(0, len(order_numbers)):
            writer.writerow({'reference_id':order_numbers[i], 'origin_city':origin_cities[i], 'origin_state':origin_states[i],
                        'origin_zip':'', 'destination_city':dest_cities[i], 'destination_state': dest_states[i],
                        'destination_zip':'', 'truck_type': 'Dry Van', 'distance': miles[i], 'pick_date': pick_dates[i],
                        'pick_time': '', 'drop_date': drop_dates[i], 'drop_time': '', 'stops': 0, 'shipper': 'GAR'})

if __name__ == "__main__":
    page = requests.get("http://www.gartran.com/main.php/current_loads?table_view=1&page_order=id&page_dir=xxx&page_num=1")
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find_all('tr')
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    csv_name = "gardata_{}.csv".format(today)

    all_trucks = [table[i].select('td')[8].get_text() for i in range(1, len(table))]
    all_miles = [table[i].select('td')[6].get_text() for i in range(1, len(table))]
    order_numbers = []
    pick_dates = []
    drop_dates = []
    origin_states = []
    origin_cities = []
    dest_states = []
    dest_cities = []
    miles = []

    print("Collecting data...")
    get_data()
    print("Done.")
    write_csv()
    print("Saved to {}".format(csv_name))
