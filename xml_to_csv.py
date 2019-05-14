"""XML to CSV Scraper."""
import sys, csv
from xml.etree import ElementTree

def main(file_path):
  tree = ElementTree.parse(file_path)
  root = tree.getroot()
  
  New_CSV = csv.writer('new_csv.csv', 'w')
  New_CSV.close()

if __name__ == '__main__':
  main(sys.argv[1])  

