

import csv
import random
import math


#abrir el archivo
def load_csv(demanda_diaria_2022):
    dataset = []
    with open(demanda_diaria_2022, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset

