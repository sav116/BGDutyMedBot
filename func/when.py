from func.base import month_name, max_day_of_month, get_weekday
import datetime

from loader import DATA_DEV, DATA_SUP, GOOGLE_DEV_SHEET_CUR_MONTH, GOOGLE_DEV_SHEET_NEXT_MONTH, \
    GOOGLE_SUP_SHEET_CUR_MONTH, GOOGLE_SUP_SHEET_NEXT_MONTH


def get_duty_datas(now, sheet, sheet_next_month, data=None, username=None):
    #print(data_sup)
    fio = data[username]['fio']
    timezone = data[username]['timezone']
    phone = data[username]['timezone']
    first_name = fio.split()[1]
    result = f"{first_name}, вы дежурите:\n"
    len_res = len(result)
    # Бежим по строкам и ищем фамилию
    max_day = max_day_of_month(
        datetime.date(now.year, now.month, 1)).day
    for row in range(3, 40):
        cell_2_value = sheet.cell(row=row, column=2).value
        if isinstance(cell_2_value, str) and fio in  cell_2_value.strip():
            # бежим по строкам и ищем даты дежурств
            for day in range(now.day+3, max_day+4):
                cell_obj = sheet.cell(row=row, column=day)
                cell_data_value = sheet.cell(row=1, column=day).value
                if cell_obj.fill.start_color.index in ('FF0000FF'):
                    str_date = cell_data_value.strftime("%d.%m.%Y")
                    weekday = get_weekday(cell_data_value.weekday())
                    result+=f"{str_date} - {weekday},\n"

    if sheet_next_month is not None:
        max_day = max_day_of_month(
            datetime.date(now.year, now.month+1, 1)).day
        for row in range(3, 40):
            cell_2_value = sheet_next_month.cell(row=row, column=2).value
            if isinstance(cell_2_value, str) and fio in  cell_2_value.strip():
                for day in range(4, max_day + 4):
                    cell_obj = sheet_next_month.cell(row=row, column=day)
                    cell_data_value = sheet_next_month.cell(row=1, column=day).value
                    if cell_obj.fill.start_color.index in ('FF0000FF'):
                        str_date = cell_data_value.strftime("%d.%m.%Y")
                        weekday = get_weekday(cell_data_value.weekday())
                        result += f"{str_date} - {weekday},\n"
    if len_res < len(result):
        return result[:-2] + '.'
    else:
        return None

def get_when(username):
    username= '@' + username
    now = datetime.datetime.now()
    if isinstance(DATA_DEV, dict):
        if username in DATA_DEV.keys():
            return get_duty_datas(now, GOOGLE_DEV_SHEET_CUR_MONTH, GOOGLE_DEV_SHEET_NEXT_MONTH, DATA_DEV, username)
    elif isinstance(DATA_SUP, dict):
        if username in DATA_SUP.keys():
            return get_duty_datas(now, GOOGLE_SUP_SHEET_CUR_MONTH, GOOGLE_SUP_SHEET_NEXT_MONTH, DATA_SUP, username)
    else:
        return None
