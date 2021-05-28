from func.base import month_name
from func.worker import google_doc_dev, google_doc_sup, forced_update
import datetime
import pprint

now=datetime.datetime.now()
forced_update()

sheet_dev = google_doc_sup[f"{month_name(now.month)} {now.year}"]

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
        cell_fio=sheet_sup.cell(row=i, column=2)
        cell_phone=sheet_sup.cell(row=i, column=3)
        cell_nick=sheet_sup.cell(row=i, column=4)
        cell_timezone=sheet.cell(row=i, column=6)
        if isinstance(cell_nick.value, str) and cell_nick.value.strip().startswith('@'):
            tg_nick=cell_nick.value.strip()
            tg_phone=cell_phone.value.strip()
            tg_fio=cell_fio.value
            tg_time_zone=cell_timezone.value.strip()
            technical_support[tg_nick]['phone']=tg_phone
            technical_support[tg_nick]['fio']=tg_fio
            technical_support[tg_time_zone]['timezone']

    pprint(technical_support)