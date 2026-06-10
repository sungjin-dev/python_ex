import os
import json

def setFilePath(fileName):  
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

    dbPath = os.path.join(BASE_PATH, 'db')

    if not os.path.exists(dbPath):
        os.makedirs(dbPath)  

    return os.path.join(dbPath, fileName)

def save_data(fileName, dict): 

    dbFilePath = setFilePath(fileName) 

    with open(dbFilePath, 'w', encoding= 'utf-8') as f:

        json.dump(dict, f, ensure_ascii = False, indent = 4)  

def load_data(fileName, dict): 

    dbFile = setFilePath(fileName) 

    if not os.path.exists(dbFile):  
        save_data(fileName, dict) 

        return dict

    with open(dbFile, 'r', encoding='utf-8') as f:
        return json.load(f)