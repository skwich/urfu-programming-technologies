import math

def CheckCorrectData(data, dataType):
    if isinstance(dataType, bool) and (data == 'да' or data == 'нет'):
        return True
    elif isinstance(dataType, int) and data.isdigit():
        return True
    elif isinstance(dataType, str) and data != '':
        return True
    else:
        return False

def InputData(textData, dataType):
    data = input(textData)
    while not CheckCorrectData(data, dataType):
        print('Данные некорректны, повторите ввод')
        data = input(textData)
    
    if isinstance(dataType, int) and data.isdigit():
        return int(data)
    elif isinstance(dataType, bool):
        return True if data == 'да' else False
    return data

def PerformDeclension(text, declensions):
    if text == 1:
        return declensions[0]
    elif text in (2, 3, 4):
        return declensions[1]
    else:
        return declensions[2]

jobName = InputData('Введите название вакансии: ', str())
jobDiscription = InputData('Введите описание вакансии: ', str())
city = InputData('Введите город для вакансии: ', str())
experience = InputData('Введите требуемый опыт работы (лет): ', int())
lowerSalaryLimit = InputData('Введите нижнюю границу оклада вакансии: ', int())
upperSalaryLimit = InputData('Введите верхнюю границу оклада вакансии: ', int())
while lowerSalaryLimit > upperSalaryLimit:
    print('Нижняя граница оклада должна быть не больше верхней границы. Повторите ввод.')
    lowerSalaryLimit = InputData('Введите нижнюю границу оклада вакансии: ', int())
    upperSalaryLimit = InputData('Введите верхнюю границу оклада вакансии: ', int())

isFlexible = InputData('Нужен свободный график (да / нет): ', bool())
isPremium = InputData('Является ли данная вакансия премиум-вакансией (да / нет): ', bool())

print(jobName)
print(f"Описание: {jobDiscription}")
print(f"Город: {city}")
print(f"Требуемый опыт работы: {experience} {PerformDeclension(experience, ['год','года','лет'])}")

roundedAvgSalary = math.floor((upperSalaryLimit+lowerSalaryLimit)/2)
print(f"Средний оклад: {roundedAvgSalary} {PerformDeclension(roundedAvgSalary, ['рубль','рубля','рублей'])}")
print(f"Свободный график: {'да' if isFlexible else 'нет'}")
print(f"Премиум-вакансия: {'да' if isPremium else 'нет'}")