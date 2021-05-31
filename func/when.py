from func.base import update_docs, month_name, max_day_of_month, get_weekday
import datetime

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
            # бежим по строкам и ищем
            for day in range(now.day+3, max_day+4):
                cell_obj = sheet.cell(row=row, column=day)
                cell_data_value = sheet.cell(row=1, column=day).value
                if cell_obj.fill.start_color.index in ('FF0000FF'):
                    print(day)
                    print(cell_data_value)
                    str_date = cell_data_value.strftime("%d.%m.%Y")
                    weekday = get_weekday(cell_data_value.weekday())
                    result+=f"{str_date} - {weekday},\n"

    if sheet_next_month is not None:
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
    sheet_dev_next_month = None
    sheet_sup_next_month = None
    try:
        GOOGLE_DEV, GOOGLE_SUP, DATA_DEV, DATA_SUP = update_docs()
        sheet_dev = GOOGLE_DEV[f"{month_name(now.month)} {now.year}"] # Open boock sheet
        sheet_sup = GOOGLE_SUP[f"{month_name(now.month)} {now.year}"]
    except:
        return 'Something went wrong'
    try:
        sheet_dev_next_month = GOOGLE_DEV[f"{month_name(now.month+1)} {now.year}"] # Open boock sheet on next month
    except:
        pass
    try:
        sheet_sup_next_month = GOOGLE_SUP[f"{month_name(now.month + 1)} {now.year}"]
    except:
        pass

    if username in DATA_DEV.keys():
        datas_str = get_duty_datas(now, sheet_dev, sheet_dev_next_month, DATA_DEV, username)
        print(datas_str)
        return datas_str
    elif username in DATA_SUP.keys():
        datas_str = get_duty_datas(now, sheet_sup, sheet_sup_next_month, DATA_SUP, username)
        print(datas_str)
        return datas_str
    else:
        return None