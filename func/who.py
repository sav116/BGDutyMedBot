import openpyxl
import time
import requests
import io
import datetime
from data.config import URL_GOOGLE_DOC_DEV, URL_GOOGLE_DOC_SUP
from func.base import month_name, max_day_of_month,update_docs


# def who_now():
#     update_docs()
#     now = datetime.datetime.now()
#     result = "Сейчас дежурные:\n"
#     try:
#         print(f"{month_name(now.month)} {now.year}")
#         sheet_dev = GOOGLE_DEV[f"{month_name(now.month)} {now.year}"]
#         sheet_sup = GOOGLE_SUP[f"{month_name(now.month)} {now.year}"]
#         #print('yes')
#     except:
#         return "bad date"
#     max_day = max_day_of_month(
#         datetime.date(now.year, now.month, 1)).day
#     return result