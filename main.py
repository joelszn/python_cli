# Raymond Baez
# Lab 5 CIS 440

import csv

def main():
    print("Hello welcome to this CSV app! First you'll need to specify a function read, write, update, & delete")
    userFunction = input("Specify function (e.g. read, write, update, & delete): ")

# if/else based logic that changes depending on user input
    if userFunction == "write":
        from writer_ import writer

        filename = input("Enter file name (e.g test.csv): ")
        header = ("Season", "Age", "PPG")
        data = [
        (1987, 23, 37),
        (1988, 24, 35),
        (1989, 25, 33),
        (1990, 26, 34)
        ]

        writer(header, data, filename, "write")

    elif userFunction == "read":
        from read import reader
        print("This will print csv")
        filename = input("Enter a file name to update (e.g test.csv): ")
        reader(filename)

    elif userFunction == "update":
        from update import updater
        print("This will update one PPG field")
        filename = input("Enter a file name to update (e.g test.csv): ")
        updater(filename)

    elif userFunction == "delete":
        from delete import remove
        print("This will remove one PPG field")
        filename = input("Enter a file name to update (e.g test.csv): ")
        remove(filename)

    else:
        print("Option does not exist. Try again")


if __name__=="__main__":
    main()
