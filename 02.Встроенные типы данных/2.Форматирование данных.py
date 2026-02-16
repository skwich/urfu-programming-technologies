import math

def PerformDeclension(text, declensions):
    if text == 1:
        return declensions[0]
    elif text in (2, 3, 4):
        return declensions[1]
    else:
        return declensions[2]

jobName = str(input('Введите название вакансии: '))
jobDiscription = str(input('Введите описание вакансии: '))
city = str(input('Введите город для вакансии: '))
experience = int(input('Введите требуемый опыт работы (лет): '))
lowerSalaryLimit = int(input('Введите нижнюю границу оклада вакансии: '))
upperSalaryLimit = int(input('Введите верхнюю границу оклада вакансии: '))
isFlexible = input('Нужен свободный график (да / нет): ') == 'да'
isPremium = input('Является ли данная вакансия премиум-вакансией (да / нет): ') == 'да'

print(jobName)
print(f"Описание: {jobDiscription}")
print(f"Город: {city}")
print(f"Требуемый опыт работы: {experience} {PerformDeclension(experience, ['год','года','лет'])}")

roundedAvgSalary = math.floor((upperSalaryLimit+lowerSalaryLimit)/2)
print(f"Средний оклад: {roundedAvgSalary} {PerformDeclension(roundedAvgSalary, ['рубль','рубля','рублей'])}")
print(f"Свободный график: {'да' if isFlexible else 'нет'}")
print(f"Премиум-вакансия: {'да' if isPremium else 'нет'}")