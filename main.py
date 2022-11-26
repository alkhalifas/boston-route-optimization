import csv

from bs4 import BeautifulSoup

from integration import process_coordinate_string, process_kml

if __name__ == "__main__":
    process_kml('data/Sample Route.kml')