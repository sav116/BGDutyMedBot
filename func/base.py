import datetime

#from func.worker import google_doc_dev, google_doc_sup

def month_name(month):
    months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    if (0 < month < 13):
        return months[month -1]
    else:
        return "====bad month==="

def working_day():
    start_work_day = datetime.time(9, 00, 00)
    end_work_day = datetime.time(18,00,00)
    now = datetime.datetime.now()
    if now.weekday() < 5 and start_work_day <= now.time() <= end_work_day:
        return True
    return False


# def get_who_duty_now(doc_dev=google_doc_dev, doc_sup=google_doc_sup):
#     pass