import csv
import re

def IsDataMoreHalf(row, header):
    filteredRow = [value for value in row if value != '']
    return len(filteredRow) >= round(len(header)/2.0)

def RemoveHtmlTags(text: str):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def ToCorrectText(text: str):
    text = RemoveHtmlTags(text)
    text = ' '.join(text.split())
    return text

def SplitListToText(info: list):
    text = ""
    for value in info:
        text += f"{value}; "
    return text[:-2]

def PrintOutput(info: list):
    for dictionary in info:
        for key in dictionary:
            text = ""
            if isinstance(dictionary[key], list):
                text = f"{key}: {SplitListToText(dictionary[key])}"
            else:
                text = f"{key}: {dictionary[key] if dictionary[key] != '' else 'Нет данных'}"
            print(ToCorrectText(text))

        if dictionary != info[-1]:
            print()

fileName = input()
header = []
info = []
newInfo = []
with open(fileName, encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        if IsDataMoreHalf(row, header):
            info.append(row)
    
    for person in info:
        dictionary = {}
        for (key, value) in zip(header, person):
            dictionary[key] = value if not value.count('\n') else value.split('\n')
        newInfo.append(dictionary)

PrintOutput(newInfo)