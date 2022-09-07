from time import sleep

import sqlalchemy as sa

from services import Cbrf, GoogleSheets
from settings import connecting_string, file_sheet_key

cbrf = Cbrf()

while True:
    # Получаем данные из таблицы, добавляем колонку стоимости в рублях и сохраняем в базу
    my_df = GoogleSheets.sheet_to_df(file_sheet_key)
    my_df['стоимость в руб.'] = round(my_df['стоимость,$'] * cbrf.currency('USD'))
    engine = sa.create_engine(connecting_string)
    connection = engine.connect()
    my_df.to_sql('orders', con=connection, if_exists='replace', index=False)
    connection.close()
    # Засыпаем на 15 сек. чтобы Google не выкинул ошибку
    sleep(15)
