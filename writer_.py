import csv
def writer(header, data, filename, option):
        with open (filename, "w", newline = "") as f:
            if option == "write":

                stats = csv.writer(f)
                stats.writerow(header)
                for x in data:
                    stats.writerow(x)
            elif option == "update":
                writer = csv.DictWriter(f, fieldnames = header)
                writer.writeheader()
                writer.writerows(data)
            else:
                print("Option is not known")
