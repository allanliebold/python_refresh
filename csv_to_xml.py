import sys
import csv
from xml.etree import ElementTree

def main(file_path):
  tree = ElementTree.parse(file_path)
