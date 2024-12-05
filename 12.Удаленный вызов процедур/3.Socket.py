import socket
import pandas as pd


def start_server():
    df = pd.read_csv("organizations.csv")
    host = "127.0.0.32"
    port = 12345
    server = socket.socket()
    server.bind((host, port))
    server.listen(5)

    client, _ = server.accept()
    while True:
        organization_name = client.recv(1024).decode()
        if organization_name == "exit":
            break
        data = df[df["Name"] == organization_name][["Website", "Country"]].to_dict(orient="records")[0]
        client.send(f"Сайт: {data['Website']}. Страна: {data['Country']}".encode())

    client.close()
    server.close()
