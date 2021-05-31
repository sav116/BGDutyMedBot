import openpyxl, io, requests, datetime
from data.config import URL_GOOGLE_DOC_DEV, URL_GOOGLE_DOC_SUP

def get_weekday(day):
    weekdays_dict={
        0:'Понедельник',
        1:'Вторник',
        2:'Среда',
        3:'Четверг',
        4:'Пятница',
        5:'Суббота',
        6:'Воскресенье'
    }
    return weekdays_dict[day]

def update_dev_dict(doc):
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
    now=datetime.datetime.now()
    developers={}
    try:
        sheet_dev = doc[f"{month_name(now.month)} {now.year}"]
    except:
        return "Can't open book's sheet"
    for i in range(15, 140):
        cell_fio=sheet_dev.cell(row=i, column=2).value # колонка с фио
        cell_phone=sheet_dev.cell(row=i, column=3).value
        cell_nick=sheet_dev.cell(row=i, column=4).value
        cell_timezone=sheet_dev.cell(row=i, column=6).value
        if isinstance(cell_nick, str):
            if cell_nick.strip().startswith('@'):
                developers[cell_nick.strip()]={
                    'phone': str(cell_phone).strip(),
                    'fio': str(cell_fio).strip(),
                    'timezone': str(cell_timezone).strip()
                }
    return developers

def update_sup_dict(doc):
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
    now = datetime.datetime.now()
    technical_support={}
    try:
        sheet_sup = doc[f"{month_name(now.month)} {now.year}"]
    except:
        return "Can't open book's sheet"
    for i in range(15, 40):
        cell_fio=sheet_sup.cell(row=i, column=2).value
        cell_phone=sheet_sup.cell(row=i, column=3).value
        cell_nick=sheet_sup.cell(row=i, column=4).value
        cell_timezone=sheet_sup.cell(row=i, column=6).value
        if isinstance(cell_nick, str):
            if cell_nick.strip().startswith('@'):
                technical_support[cell_nick.strip()]={
                    'phone': str(cell_phone).strip(),
                    'fio': str(cell_fio).strip(),
                    'timezone': str(cell_timezone).strip()
                }
    return technical_support

def update_docs():
    GOOGLE_DEV = None
    GOOGLE_SUP = None
    response1 = requests.get(
        URL_GOOGLE_DOC_DEV,
        stream=True)
    google_doc_dev = openpyxl.load_workbook(filename=io.BytesIO(response1.content), data_only=True)
    DATA_DEV = update_dev_dict(google_doc_dev)
    response2 = requests.get(
        URL_GOOGLE_DOC_SUP,
        stream=True)
    google_doc_sup = openpyxl.load_workbook(filename=io.BytesIO(response2.content), data_only=True)
    DATA_SUP = update_sup_dict(google_doc_sup)
    return google_doc_dev, google_doc_sup, DATA_DEV, DATA_SUP

def month_name(month):
    months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    if (0 < month < 13):
        return months[month -1]
    else:
        return "====bad month==="

def max_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)

def working_day():
    start_work_day = datetime.time(9, 00, 00)
    end_work_day = datetime.time(18,00,00)
    now = datetime.datetime.now()
    if now.weekday() < 5 and start_work_day <= now.time() <= end_work_day:
        return True
    return False
