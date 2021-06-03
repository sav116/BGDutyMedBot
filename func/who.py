import datetime
from func.base import month_name, max_day_of_month, get_nic_telegramm
from loader import GOOGLE_SUP_SHEET_CUR_MONTH


def who_duty_dev():
    pass

def who_duty_sup():
    now = datetime.datetime.now()
    max_day = max_day_of_month(
        datetime.date(now.year, now.month, 1)).day
    parse_mode = False
    column_day = now.day + 3
    cell_data_value = GOOGLE_SUP_SHEET_CUR_MONTH.cell(row=1, column=column_day).value
    if now.date() == cell_data_value.date():
        for row in range(2, 30):
            color = GOOGLE_SUP_SHEET_CUR_MONTH.cell(row=row, column=now.day+3).fill.start_color.index
            try:
                if '18' in GOOGLE_SUP_SHEET_CUR_MONTH.cell(row=row, column=2).value:
                    parse_mode = True
            except:
                pass
            try:
                if '7' in GOOGLE_SUP_SHEET_CUR_MONTH.cell(row=row, column=2).value:
                    parse_mode = False
            except:
                pass
            if color == "FF0000FF" and parse_mode:
                duty_fio = GOOGLE_SUP_SHEET_CUR_MONTH.cell(row=row, column=2).value.strip()
                surname = duty_fio.split()[0]
                first_name = duty_fio.split()[1]
                duty_nick = get_nic_telegramm(duty_fio, GOOGLE_SUP_SHEET_CUR_MONTH)
                if duty_nick is not None:
                    return f"Сейчас дежурный 1 линии:\n{surname} {first_name} {duty_nick}"
                elif duty_nick is None:
                    return "Дежурный 1 линии не найден"
    return "Дежурный 1 линии не найден"