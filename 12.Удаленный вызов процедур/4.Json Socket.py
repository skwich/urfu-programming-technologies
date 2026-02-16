import socket
import json
import pandas as pd


def get_website(df, name):
    return str(df[df["Name"] == name].iloc[0]["Website"])


def get_country(df, name):
    return str(df[df["Name"] == name].iloc[0]["Country"])


def get_number_of_employees(df, name):
    return str(df[df["Name"] == name].iloc[0]["Number of employees"])


def get_description(df, name):
    return str(df[df["Name"] == name].iloc[0]["Description"])


def execute_func(df, json_row):
    match json_row["operation"]:
        case "get_website":
            return get_website(df, json_row["name"])
        case "get_country":
            return get_country(df, json_row["name"])
        case "get_number_of_employees":
            return get_number_of_employees(df, json_row["name"])
        case "get_description":
            return get_description(df, json_row["name"])


def start_server():
    df = pd.read_csv("organizations.csv")
    host = "127.0.0.32"
    port = 12345

    server = socket.socket()
    server.bind((host, port))
    server.listen(5)

    client, _ = server.accept()
    while True:
        client_message = client.recv(1024).decode()
        if not client_message:
            break
        json_row = json.loads(client_message)
        result = execute_func(df, json_row)
        client.send(json.dumps({"result": result}).encode())

    client.close()
    server.close()
