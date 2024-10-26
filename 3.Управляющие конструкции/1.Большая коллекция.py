import csv

fileName = input()
header = []
info = []

with open(fileName, encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        filteredRow = [value for value in row if value != '']
        if len(filteredRow) >= round(len(header)/2.0):
            info.append(row)
print(header)
print(info)