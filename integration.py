from bs4 import BeautifulSoup
import csv


def process_coordinate_string(input_str):
    # Take the coordinate string from the KML file, and break it up into [Lat,Lon,Lat,Lon...] for a CSV row
    input_str = input_str.replace('\n', '')
    input_str = input_str.replace('\r', '')
    input_str = input_str.replace('\t', '')
    results = []
    space_split = input_str.split(' ')
    # print("space_split: ", space_split)
    for dim in space_split:
        coordinates = dim.split(",")
        if len(coordinates) > 1:
            # print("coordinates: ", coordinates)
            results.append([float(coordinates[0]), float(coordinates[1]), float(coordinates[1])])

    return results


def process_kml(input_file_name):
    # Open the KML. Read the KML. Open a CSV file. Process a coordinate string to be a CSV row.
    # print("input_file_name: ", input_file_name)
    output_file_name = input_file_name.split('.')[0] + ".csv"

    # print("output_file_name: ", output_file_name)
    with open(input_file_name, 'r') as f:
        s = BeautifulSoup(f, 'xml')
        # print("s: ", s)

    with open(output_file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for coords in s.find_all('coordinates'):
            print("coords: ", coords)
            print("len(coords): ", len(coords))
            results = process_coordinate_string(coords.string)
            for result in results:
                writer.writerow(result)
