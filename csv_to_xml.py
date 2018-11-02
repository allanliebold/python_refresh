import sys
import csv
from xml.etree import ElementTree

def main(file_path):
  tree = ElementTree.parse(file_path)

if __name__ == '__main__':
  main(sys.argv[1])  
