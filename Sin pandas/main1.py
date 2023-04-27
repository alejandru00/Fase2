

import csv
import random
import math


# abrir el archivo y leerlo
def load_csv(demanda_diaria_2022):
    dataset = []
    with open(demanda_diaria_2022, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset


# ordena data set quitando los blancos
def summarize(dataset):
    summaries = [(column, min(values), max(values), len(values), sum(values) / len(values)) for column, values in enumerate(zip(*dataset))]
    del summaries[-1]                   # quita los blancos de la columna
    return summaries 


# da la longitud de cada dataset y cuenta los datos de cada archivo
def split_data(dataset, split_ratio):
    train_size = int(len(dataset) * split_ratio)
    train_set = []
    test_set = list(dataset)
    while len(train_set) < train_size:
        index = random.randrange(len(test_set))
        train_set.append(test_set.pop(index))
    return train_set, test_set
