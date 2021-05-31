from func.base import update_docs, month_name, max_day_of_month, get_weekday
import datetime

def get_duty_datas_dev(now, sheet_dev, sheet_dev_next_month, data_dev=None, username=None):
    fio = data_dev[username]['fio']
    timezone = data_dev[username]['timezone']
    phone = data_dev[username]['timezone']
    first_name = fio.split()[1]
    result = f"{first_name}, вы дежурите:\n"
    # Бежим по строкам и ищем фамилию
    max_day = max_day_of_month(
        datetime.date(now.year, now.month, 1)).day
    for row in range(3, 40):
        cell_2_value = sheet_dev.cell(row=row, column=2).value
        if isinstance(cell_2_value, str) and cell_2_value.strip() == fio:
            for day in range(now.day + 3, max_day + 4):
                cell_obj = sheet_dev.cell(row=row, column=day)
                cell_data_value = sheet_dev.cell(row=3, column=day).value
                if cell_obj.fill.start_color.index in ('FF0000FF'):
                    str_date = cell_data_value.strftime("%d.%m.%Y")
                    weekday = get_weekday(cell_data_value.weekday())
                    result += f"{str_date} - {weekday},\n"

    if sheet_dev_next_month is not None:
        for row in range(3, 40):
            cell_2_value = sheet_dev_next_month.cell(row=row, column=2).value
            if isinstance(cell_2_value, str) and cell_2_value.strip() == fio:
                for day in range(now.day + 3, max_day + 4):
                    cell_obj = sheet_dev.cell(row=row, column=day)
                    cell_data_value = sheet_dev.cell(row=3, column=day).value
                    if cell_obj.fill.start_color.index in ('FF0000FF'):
                        str_date = cell_data_value.strftime("%d.%m.%Y")
                        weekday = get_weekday(cell_data_value.weekday())
                        result += f"{str_date} - {weekday},\n"
    return result[:-2]

def get_duty_datas_sup(now, sheet_sup, sheet_dev_next_month, data_sup=None, username=None):
    fio = data_sup[username]['fio']
    timezone = data_sup[username]['timezone']
    phone = data_sup[username]['timezone']
    first_name = fio.split()[1]
    result = f"{first_name}, вы дежурите:\n"
    # Бежим по строкам и ищем фамилию
    max_day = max_day_of_month(
        datetime.date(now.year, now.month, 1)).day
    for row in range(3, 40):
        cell_2_value = sheet_sup.cell(row=row, column=2).value
        if isinstance(cell_2_value, str) and cell_2_value.strip() == fio:
            for day in range(now.day+3, max_day+4):
                cell_obj = sheet_sup.cell(row=row, column=day)
                cell_data_value = sheet_sup.cell(row=3, column=day).value
                if cell_obj.fill.start_color.index in ('FF0000FF'):
                    str_date = cell_data_value.strftime("%d.%m.%Y")
                    weekday = get_weekday(cell_data_value.weekday())
                    result+=f"{str_date} - {weekday},\n"

    if sheet_dev_next_month is not None:
        for row in range(3, 40):
            cell_2_value = sheet_dev_next_month.cell(row=row, column=2).value
            if isinstance(cell_2_value, str) and cell_2_value.strip() == fio:
                for day in range(now.day + 3, max_day + 4):
                    cell_obj = sheet_sup.cell(row=row, column=day)
                    cell_data_value = sheet_sup.cell(row=3, column=day).value
                    if cell_obj.fill.start_color.index in ('FF0000FF'):
                        str_date = cell_data_value.strftime("%d.%m.%Y")
                        weekday = get_weekday(cell_data_value.weekday())
                        result += f"{str_date} - {weekday},\n"
    return result[:-2]

def get_when(username):
    username= '@' + username
    result = ''
    now = datetime.datetime.now()
    sheet_dev_next_month = None
    sheet_sup_next_month = None
    try:
        GOOGLE_DEV, GOOGLE_SUP, DATA_DEV, DATA_SUP = update_docs()
        sheet_dev = GOOGLE_DEV[f"{month_name(now.month)} {now.year}"] # Open boock sheet
        sheet_sup = GOOGLE_SUP[f"{month_name(now.month)} {now.year}"]
    except:
        return 'Something went wrong'
    try:
        sheet_dev_next_month = GOOGLE_DEV[f"{month_name(now.month)} {now.year}"] # Open boock sheet on next month
        sheet_sup_next_month = GOOGLE_SUP[f"{month_name(now.month)} {now.year}"]
    except:
        pass

    if username in DATA_DEV.keys():
        datas_str = get_duty_datas_dev(now, sheet_dev, sheet_dev_next_month, DATA_DEV, username)
        print(datas_str)
        return datas_str
    elif username in DATA_SUP.keys():
        datas_str = get_duty_datas_sup(now, sheet_sup, sheet_sup_next_month, DATA_DEV, username)
        print(datas_str)
        return datas_str
    else:
        return None