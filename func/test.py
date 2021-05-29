from func.base import month_name
import datetime
import pprint
from data.config import URL_GOOGLE_DOC_DEV, URL_GOOGLE_DOC_SUP
import requests
import openpyxl
import io

now=datetime.datetime.now()

google_doc_dev=None
google_doc_sup=None

def forced_update():
    global google_doc_dev, google_doc_sup
    response1 = requests.get(
        URL_GOOGLE_DOC_DEV,
        stream=True)
    google_doc_dev = openpyxl.load_workbook(filename=io.BytesIO(response1.content), data_only=True)

    response2 = requests.get(
        URL_GOOGLE_DOC_SUP,
        stream=True)
    google_doc_sup = openpyxl.load_workbook(filename=io.BytesIO(response2.content), data_only=True)
    print('Google таблицы обновлены принудительно')
forced_update()

sheet_sup = google_doc_sup[f"{month_name(now.month)} {now.year}"]

technical_support = {}

def _update_sup_dict(sheet):
    """
        developers = {
            '@username':
                {
                    'phone': '790000000',
                    'fio': 'Ivanov Ivan Ivanovich',
                    'timezone': 'МСК+0'
                }
        }
        """
    global technical_support
    try:
        sheet_sup = google_doc_sup[f"{month_name(now.month)} {now.year}"]
    except:
        return "Can't open book's sheet"
    for i in range(15, 40):
        cell_fio=sheet_sup.cell(row=i, column=2).value
        cell_phone=sheet_sup.cell(row=i, column=3).value
        cell_nick=sheet_sup.cell(row=i, column=4).value
        cell_timezone=sheet.cell(row=i, column=6).value
        if isinstance(cell_nick, str):
            if cell_nick.strip().startswith('@'):
                tg_nick=cell_nick.strip()
                tg_phone=str(cell_phone).strip()
                tg_fio=str(cell_fio).strip()
                tg_time_zone=str(cell_timezone).strip()
                technical_support[tg_nick]={
                    'phone': tg_phone,
                    'fio': tg_fio,
                    'timezone': tg_time_zone
                }


_update_sup_dict(sheet_sup)