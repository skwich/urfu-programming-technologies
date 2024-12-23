jobName = str(input('Введите название вакансии: '))
jobDiscription = str(input('Введите описание вакансии: '))
city = str(input('Введите город для вакансии: '))
experience = int(input('Введите требуемый опыт работы (лет): '))
lowerSalaryLimit = int(input('Введите нижнюю границу оклада вакансии: '))
upperSalaryLimit = int(input('Введите верхнюю границу оклада вакансии: '))
isFlexible = input('Нужен свободный график (да / нет): ') == 'да'
isPremium = input('Является ли данная вакансия премиум-вакансией (да / нет): ') == 'да'

print(f"{jobName} ({type(jobName).__name__})")
print(f"{jobDiscription} ({type(jobDiscription).__name__})")
print(f"{city} ({type(city).__name__})")
print(f"{experience} ({type(experience).__name__})")
print(f"{lowerSalaryLimit} ({type(lowerSalaryLimit).__name__})")
print(f"{upperSalaryLimit} ({type(upperSalaryLimit).__name__})")
print(f"{isFlexible} ({type(isFlexible).__name__})")
print(f"{isPremium} ({type(isPremium).__name__})")