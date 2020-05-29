import csv
from writer_ import writer  # importing writer fcn from writer_.py

def remove(filename):
    with open(filename, newline= "") as file:
        readData = [row for row in csv.DictReader(file)]
        readData[0]['PPG'] = ''

    readHeader = readData[0].keys()
    writer(readHeader, readData, filename, "update")
