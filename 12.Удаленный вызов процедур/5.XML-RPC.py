from xmlrpc.server import SimpleXMLRPCServer
import pandas as pd


def get_vacancy_by_id(id):
    global df
    values = df[df.index == id][["name", "from", "to", "city"]].values.tolist()[0]
    return {
        "Название вакансии": values[0],
        "Зарплата от": values[1],
        "Зарплата до": values[2],
        "Город": values[3],
    }


def get_vacancies_by_city(city):
    return get_vacancies_by("city", city)


def get_vacancies_by_min_salary(salary):
    return get_vacancies_by("from", salary)


def get_vacancies_by(by, param):
    global df
    copy_df = df.copy(deep=True)
    if by == "city":
        copy_df = copy_df[copy_df[by] == param][["name", "from", "to", "city"]]
    else:
        copy_df = copy_df[copy_df[by] >= param][["name", "from", "to", "city"]]
    copy_df.columns = ["Название вакансии", "Зарплата от", "Зарплата до", "Город"]
    d = copy_df.to_dict(orient="index")
    return {str(key): value for (key, value) in d.items()}


def exit():
    global stop_server
    stop_server = True


def start_server():
    global df
    global stop_server
    df = pd.read_csv("vacancies.csv", names=["name", "from", "to", "cur", "city", "date"])
    stop_server = False

    with SimpleXMLRPCServer(("localhost", 8000), allow_none=True) as server:
        server.register_function(get_vacancy_by_id)
        server.register_function(get_vacancies_by_city)
        server.register_function(get_vacancies_by_min_salary)
        server.register_function(exit)
        while not stop_server:
            server.handle_request()
