import datetime
from func.base import get_nic_telegramm, get_nic_telegramm_dev


def who_duty_dev():
    from loader import GOOGLE_SUP_SHEET_CUR_MONTH, GOOGLE_DEV_SHEET_CUR_MONTH, DATA_DEV
    global duty_direction_1, duty_direction_2
    now = datetime.datetime.now()
    # Определяемся какая по счету синяя ячейка нас интересует
    parse_mode = None
    if now.time() <= datetime.time(5, 00, 00):
        parse_mode = 1  # 00:00 - 5:00 МСК
    elif now.time() > datetime.time(18, 00, 00):
        parse_mode = 2  # 18:00 - 00:00 МСК

    column_day = now.day + 3
    cell_data_value = GOOGLE_DEV_SHEET_CUR_MONTH.cell(row=1, column=column_day).value
    counter = 0
    if now.date() == cell_data_value.date():
        for row in range(2, 43):
            color = GOOGLE_DEV_SHEET_CUR_MONTH.cell(row=row, column=now.day + 3).fill.start_color.index
            if color == "FF0000FF":
                counter += 1
                if counter == parse_mode:
                    duty_fio = GOOGLE_DEV_SHEET_CUR_MONTH.cell(row=row, column=2).value.strip()

                    if ',' not in duty_fio:
                        surname = duty_fio.split()[0]
                        first_name = duty_fio.split()[1]
                        duty_nick = get_nic_telegramm_dev(duty_fio, GOOGLE_DEV_SHEET_CUR_MONTH)
                        return f"Сейчас дежурный 3 линии:\n{surname} {first_name} {duty_nick}."

                    elif ',' in duty_fio:
                        duty_fio_1 = duty_fio.split(',')[0].strip()
                        surname_1 = duty_fio_1.split()[0]
                        first_name_1 = duty_fio_1.split()[1]
                        duty_nick_1 = get_nic_telegramm_dev(duty_fio_1, GOOGLE_DEV_SHEET_CUR_MONTH)
                        duty_direction_1 = None
                        if duty_nick_1 is not None:
                            duty_direction_1 = DATA_DEV[duty_nick_1]['direction']
                        duty_fio_2 = duty_fio.split(',')[1].strip()
                        surname_2 = duty_fio_2.split()[0]
                        first_name_2 = duty_fio_2.split()[1]
                        duty_nick_2 = get_nic_telegramm_dev(duty_fio_2, GOOGLE_DEV_SHEET_CUR_MONTH)
                        duty_direction_2 = None
                        if duty_nick_2 is not None:
                            duty_direction_2 = DATA_DEV[duty_nick_2]['direction']

                        return f"Сейчас дежурные 3 лини:\n" \
                               f"{duty_direction_1} - {surname_1} {first_name_1} {duty_nick_1},\n" \
                               f"{duty_direction_2} - {surname_2} {first_name_2} {duty_nick_2}."

    return "Дежурный 3 линии не найден"


def who_duty_sup_weekday():
    from loader import GOOGLE_SUP_SHEET_CUR_MONTH, GOOGLE_DEV_SHEET_CUR_MONTH, DATA_DEV
    now = datetime.datetime.now()

    parse_mode = False
    column_day = now.day + 3
    cell_data_value = GOOGLE_SUP_SHEET_CUR_MONTH.cell(row=1, column=column_day).value
    if now.date() == cell_data_value.date():
        for row in range(2, 30):
            color = GOOGLE_SUP_SHEET_CUR_MONTH.cell(row=row, column=now.day + 3).fill.start_color.index
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


def who_duty_sup_dayoff():
    from loader import GOOGLE_SUP_SHEET_CUR_MONTH, GOOGLE_DEV_SHEET_CUR_MONTH, DATA_DEV
    global parse_mode
    now = datetime.datetime.now()

    # Определяемся какая по счету синяя ячейка нас интересует
    if now.time() > datetime.time(18, 00, 00):
        parse_mode = 1  # 18:00 - 00:00 МСК
    elif now.time() < datetime.time(7, 00, 00):
        parse_mode = 2  # 00:00 - 7:00 МСК
    elif datetime.time(7, 00, 00) <= now.time() <= datetime.time(18, 00, 00):
        parse_mode = 3  # 07:00 - 18:00 МСК

    column_day = now.day + 3
    cell_data_value = GOOGLE_SUP_SHEET_CUR_MONTH.cell(row=1, column=column_day).value
    counter = 0
    if now.date() == cell_data_value.date():
        for row in range(2, 30):
            color = GOOGLE_SUP_SHEET_CUR_MONTH.cell(row=row, column=now.day + 3).fill.start_color.index
            if color == "FF0000FF":
                counter += 1
                if counter == parse_mode:
                    duty_fio = GOOGLE_SUP_SHEET_CUR_MONTH.cell(row=row, column=2).value.strip()
                    surname = duty_fio.split()[0]
                    first_name = duty_fio.split()[1]
                    duty_nick = get_nic_telegramm(duty_fio, GOOGLE_SUP_SHEET_CUR_MONTH)
                    if duty_nick is not None:
                        return f"Сейчас дежурный 1 линии:\n{surname} {first_name} {duty_nick}"
                    elif duty_nick is None:
                        return "Дежурный 1 линии не найден"
    return "Дежурный 1 линии не найден"
