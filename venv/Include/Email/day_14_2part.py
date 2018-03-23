import csv

# newline='' es importante porque sino hace un doble salto de linea

with open("cvs\data.csv", "w+",newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Description", "Col 3"])
    writer.writerow(["Row1", "Some desc","Anohoder"])
    writer.writerow(["Row2", "Some desc","Another"])

with open("cvs\data.csv", "a",newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Row3", "Some desc","Anohoder"])
    writer.writerow(["Row4", "Some desc","Another"])


with open("cvs\data.csv", "r",newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)


with open("cvs\data.csv", "r",newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)


with open("cvs\data.csv", "a",newline='') as csvfile:
    fieldnamesw = ["Title", "Description", "Col 3"]
    writer = csv.DictWriter(csvfile,fieldnames=fieldnamesw)
    writer.writerow({"Title":"Row5", "Description": "Some desc","Col 3":"Anohoder"})
    writer.writerow({"Title": "Row6", "Description": "Some desc", "Col 3": "Anohoder"})

with open("cvs\data2.csv", "a",newline='') as csvfile:
    fieldnamesw = ["Title", "Description", "Col 3"]
    writer = csv.DictWriter(csvfile,fieldnames=fieldnamesw)
    writer.writeheader()
    writer.writerow({"Title":"Row5", "Description": "Some desc","Col 3":"Anohoder"})
    writer.writerow({"Title": "Row6", "Description": "Some desc", "Col 3": "Anohoder"})