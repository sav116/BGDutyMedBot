import openpyxl
import time
import requests
import io
import datetime

from data.config import URL_GOOGLE_DOC_DEV, URL_GOOGLE_DOC_SUP
from func.base import month_name

google_doc_dev = None
google_doc_sup = None

developers = {}
technical_support = {}

def update_dev_dict():
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
    global developers
    now=datetime.datetime.now()
    try:
        sheet=google_doc_dev[f"{month_name(now.month)} {now.year}"]
    except:
        return "bad date"


def update_sup_dict():
    global technical_support

def update_docs():
    while True:
        global google_doc_dev, google_doc_sup
        response1=requests.get(
            URL_GOOGLE_DOC_DEV,
            stream=True)
        google_doc_dev=openpyxl.load_workbook(filename=io.BytesIO(response1.content), data_only=True)
        update_dev_dict()

        response2=requests.get(
            URL_GOOGLE_DOC_SUP,
            stream=True)
        google_doc_sup=openpyxl.load_workbook(filename=io.BytesIO(response2.content), data_only=True)
        update_sup_dict()
        print('Google таблицы загружены в оперативную память')
        time.sleep(300)

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