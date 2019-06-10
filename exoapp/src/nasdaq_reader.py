import csv

def salmon_index(file_name):
    # Reads and transforms csv-file
    with open(file_name, 'r') as csv_file:
        # Reads the csv file
        csv_reader = csv.reader(csv_file)

        # Deletes the first lines in the public downloadable file
        foo = list(range(6))
        iterator = iter(foo)
        for bar in iterator:
            next(csv_reader)

        list_class = []
        list_average = []
        weight_classes = ['1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9+']
        for line in csv_reader:
            week = line[0] + 'w' + line[1]
            dict_average = {}
            dict_average['week'] = week
            dict_average['volume'] = line[20]
            dict_average['price'] = line[21]
            list_average.append(dict_average)
            for weight_class in weight_classes:
                dict_class = {}
                dict_class['week'] = week
                dict_class['weight_class'] = weight_class
                index = weight_classes.index(weight_class)
                # If price record is empty
                if line[index + 2]:
                    dict_class['price'] = line[index + 2]
                else:
                    dict_class['price'] = None
                if line[index + 11]:
                    dict_class['distribution'] = line[index + 11]
                else:
                    dict_class['distribution'] = None
                if line[index + 22]:
                    dict_class['standard_deviation'] = line[index + 22]
                else:
                    dict_class['standard_deviation'] = None
                list_class.append(dict_class)

        dict_result = {}
        dict_result['list_class'] = list_class
        dict_result['list_average'] = list_average

    # res = {list_class: list_class, list_average = list_average}

    return dict_result