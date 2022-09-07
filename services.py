import datetime
import json
import os

import requests
import xmltodict
import gspread as gs
import pandas as pd

from settings import key_filename


class Cbrf:
    """Запрос курса валют на сайте ЦБ РФ"""
    json_file = 'currency.json'
    url_cbr = 'https://www.cbr.ru/scripts/XML_daily.asp'

    def currency(self, request_code: str) -> float:
        # Так как курс обновляется 1 раз в сутки - проверям время последнего изменения файла
        # Если курс вчерашний обновляем, тем самым сокращаем запросы на сервер до 1 в сутки
        t = os.path.getatime(self.json_file)
        file_date = datetime.date.fromtimestamp(t)
        if any([
            datetime.date.today() > file_date,
            not os.stat(self.json_file).st_size
        ]):
            cbr_currency = xmltodict.parse(requests.get(self.url_cbr).text)
            with open(self.json_file, 'w') as js_file:
                json.dump(cbr_currency, js_file)
        # Получем из фйла сегодняшний курс и выдаем по коду запроса
        curses = {}
        key = val = None
        with open(self.json_file, 'r') as js_file:
            cbr_currency = json.load(js_file)
        for val_dict in cbr_currency['ValCurs']['Valute']:
            for _ in val_dict:
                key = val_dict['CharCode']
                val = float(val_dict['Value'].replace(',', '.'))
            curses[key] = val
        return curses[request_code]


class GoogleSheets:
    """Работа с таблицами Google по API"""

    @staticmethod
    def sheet_to_df(file_key: str, sheet: int = 0) -> pd.DataFrame:
        # Чтение таблицы в pandas DataFrame (sheet - номер листа)
        gc = gs.service_account(filename=key_filename)
        my_sheet = gc.open_by_key(file_key).get_worksheet(sheet).get_all_records()
        df = pd.DataFrame.from_dict(my_sheet)
        return df.head(len(my_sheet))
