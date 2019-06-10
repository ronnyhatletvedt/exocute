import csv

def reader():
    # Reads and transforms csv-file
    file_name = '/Users/ronny/PycharmProjects/exocute/data/exo_weightclasses.csv'
    with open(file_name, 'r') as csv_file:
        # Reads the csv file
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            something = 'test'