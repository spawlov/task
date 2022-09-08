from time import sleep

import sqlalchemy as sa
from loguru import logger

from services import Cbrf, GoogleSheets
from settings import connecting_string, file_sheet_key

cbrf = Cbrf()
logger.info('Starting task...')

# Получаем данные из таблицы, добавляем колонку стоимости в рублях и сохраняем в базу
my_df = GoogleSheets.sheet_to_df(file_sheet_key)
my_df['стоимость в руб.'] = round(my_df['стоимость,$'] * cbrf.currency('USD'))
engine = sa.create_engine(connecting_string)
logger.info('Connection to DB...')
connection = engine.connect()
logger.info('Saving DF...')
my_df.to_sql('orders', con=connection, if_exists='replace', index=False)

# Засыпаем на 5 сек. чтобы Google не выкинул ошибку
logger.info('DF is saved.\nSleeping...')
connection.close()
sleep(5)
