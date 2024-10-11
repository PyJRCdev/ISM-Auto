import json
import os

file_data = "user_data.json"

def save_data(email, password, recordar):
    if recordar:
        datos = {"email": email, "password": password}
        with open(file_data, 'w') as archivo:
            json.dump(datos, archivo)
    else:
        if os.path.exists(file_data):
            os.remove(file_data)

def load_data():
    if os.path.exists(file_data):
        with open(file_data, 'r') as archivo:
            return json.load(archivo)
    return None
