import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Подключение к базе данных
DATABASE = os.getenv('NAME_DB')
USER = os.getenv('USER_DB')
PASSWORD = os.getenv('PASSWORD_DB')
HOST = os.getenv('HOST_DB')
PORT = os.getenv('PORT_DB')

connecting_string = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

# Ключ файла таблицы
file_sheet_key = os.getenv('SHEET_KEY')

# Google key
key_filename = 'mytesttask.json'
