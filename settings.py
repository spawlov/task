import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Подключение к базе данных
# docker run -d -e POSTGRES_DB=task -e POSTGRES_USER=task -e POSTGRES_PASSWORD=task -p 5432:5432 --name my-postgres postgres

DATABASE = os.getenv('NAME_DB')
USER = os.getenv('USER_DB')
PASSWORD = os.getenv('PASSWORD_DB')
HOST = os.getenv('HOST_DB')
PORT = os.getenv('PORT_DB')

connecting_string = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
# connecting_string = f'postgresql+psycopg2://task:task@db:5432/task'

# Ключ файла таблицы
file_sheet_key = os.getenv('SHEET_KEY')

# Google key
key_filename = 'mytesttask.json'
