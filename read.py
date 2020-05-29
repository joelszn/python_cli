import csv

def reader(filename):
    with open(filename, newline= "") as file:
        reader = csv.reader(file)

        for  row in reader:
            print(row)
