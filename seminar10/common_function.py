import json
import datetime
import os.path
import view

'''
Получение даты из строки
'''
def date(date_str, len_date):
    return datetime.datetime.strptime(date_str,"%d.%m.%Y").strftime("%d.%m.%Y")

'''
Проверка строкового поля
'''
def str_len(data_str, len_str):
    try:
        if type(data_str) != str:
            data_str = str(data_str)
        if len(data_str) > len_str:
            raise ValueError
    except:
        print('Ошибка формата')
        return False
    else:
        return data_str

'''
Проверка целочисленного поля
'''
def int_len(data_int, len_int):
    try:
        if type(data_int) != int:
            data_int = int(data_int)
        if len(str(data_int)) > len_int:
            raise ValueError
    except:
        print('Ошибка формата')
        return False
    else:
        return data_int

'''
Проверка номера телефона
'''
def phone(phone_str, len_phone):
    if phone_str.isnumeric() and len(phone_str) <= len_phone:
        return phone_str
    else:
        print('Номер телефона должен быть не более 11 цифр')
        return False

'''
загрузка таблицы из БД по bd_path
'''
def bd_load(bd_path):
    if os.path.exists(bd_path):
        with open(bd_path, 'r', encoding='utf8') as fr:
            bd = json.load(fr)
        fr.close()
        return bd
    else:
        return False

'''
Нахождение значения primary_key таблицы БД bd_path
'''
def primary_get_id(bd_path, primary_key):
    id = primary_key[1]
    if id == 0:
        bd = bd_load(bd_path)
        if bd:
            for item in bd:
                if item[primary_key[0]] > id:
                    id = item[primary_key[0]]
        else:
            id = 0
    return id

'''
Устанавливаем новое текущее значение primary_key
'''
def primary_set_id(primary_key, id_value):
    primary_key[1] = id_value

'''
Генератор для получения поля из модели для запроса через Telegram 
'''
def get_field_model(record_new, bd_path, model_record, primary_key):
    count = len(model_record)
    keys = list(model_record.keys())
    values = list(model_record.values())
    i = 0
    while i < count:
        # Проверяем что у записи нет идентификатора и присваиваем следующий по номеру идентификатор
        if keys[i] == primary_key[0] and record_new[keys[i]]:
            pass
        elif keys[i] == primary_key[0]:
            record_new[keys[i]] = values[i][0](values[i][4](bd_path, primary_key), values[i][2]) + 1
        else:
            yield keys[i]
        i += 1

'''
добавление новой записи в БД bd_path в соответствии с моделью данных model_record
'''
def record_add(bd_path, model_record, primary_key):
    record_new = dict.fromkeys(model_record.keys())
    try:
        for key_field, field_value in model_record.items():
            if key_field == primary_key[0]:
                record_new[key_field] = field_value[0](field_value[4](bd_path, primary_key), field_value[2]) + 1
            else:
                record_new[key_field] = field_value[0](input(f'{field_value[1].capitalize()},'
                                                            f' не более {field_value[2]}'
                                                            f' символов: '),field_value[2])
                if not record_new[key_field]:
                    raise ValueError
    except:
        print('Ошибка в формате данных. Новые данные не сохранены.')
        return False
    else:
        if bd_data_add(bd_path,record_new):
            primary_set_id(primary_key, record_new[primary_key[0]])
            return record_new[primary_key[0]]
        else:
            print(f'Ошибка добавления новой записи в БД {bd_path}')
            return False

'''
Удаление записи из БД
'''
def record_del(id, bd_path, primary_key):
    db_record = bd_load(bd_path)
    try:
        for item in db_record:
            if item[primary_key[0]] == id:
                db_record.remove(item)
                if bd_data_save(bd_path, db_record):
                    print(f'Данные записи с № {id} удалены из БД {bd_path}')
                    return True
                else:
                    raise
    except:
        print(f'Ошибка при удаления записи с № {id} из БД {bd_path}')
        return False
    else:
        print(f'Запись с № {id} не найдена в БД {bd_path}')
        return False

'''
Изменение данных записи в БД bd_path по его id
'''
def record_change(id, bd_path, model_record, primary_key):
    record_index = -1
    bd_record = bd_load(bd_path)
    try:
        for i in range(len(bd_record)):
            if bd_record[i][primary_key[0]] == id:
                record_index = i
                break
    except:
        print(f'Ошибка чтения данных записи с № {id}')
        return False
    if record_index != -1:
        view.view_data(bd_record[record_index],model_record)
        try:
            for key_field, field_value in model_record.items():
                if key_field == primary_key[0]:
                    continue
                else:
                    new_value = input(f'При необходимости введите новое значение {field_value[1].capitalize()}, не более {field_value[2]} символов: ')
                    # если изменения есть, то проверяем формат и сохраняем в списке
                    if new_value:
                        bd_record[record_index][key_field] = field_value[0](new_value, field_value[2])
                        if not bd_record[record_index][key_field]:
                            raise ValueError
        except:
            print(f'Ошибка в формате измененных данных записи с № {id}. Данные записи не изменены.')
        else:
            if bd_data_save(bd_path, bd_record):
                return True
            else:
                print(f'Ошибка изменения данных записи с № {id} в БД')
                return False
    else:
        print(f'Запись с № {id} не найдена')
        return False

'''
Добавление данных data в таблицу БД bd_path
'''
def bd_data_add(bd_path, data):
    try:
        bd = bd_load(bd_path)
        if bd:
            bd.append(data)
        else:
            bd = []
            bd.append(data)
        if not bd_data_save(bd_path, bd):
            raise
    except:
        print(f'Ошибка добавления данных в {bd_path}')
        return False
    else:
        return True

'''
Перезапись данных data таблицы БД bd_path
'''
def bd_data_save(bd_path, data):
    try:
        with open(bd_path, 'w', encoding='utf8') as fw:
            json.dump(data, fw, ensure_ascii=False, indent=2)
    except:
        print(f'Ошибка записи данных в {bd_path}')
        return False
    else:
        return True
    finally:
        fw.close()

'''
Получение записи из БД по id
'''
def record_get_id(id, bd_path, primary_key):
    db_record = bd_load(bd_path)
    try:
        for item in db_record:
            if item[primary_key[0]] == id:
                return item
    except:
        print(f'Ошибка поиска записи с № {id} в БД {bd_path}')
        return False
    else:
        print(f'Запись с № {id} не найдена в БД {bd_path}')
        return False
'''
Запись данных в БД для Телеграм
'''
def record_save_telegram(record_model, bd_path, primary_key):
    bd = bd_load(bd_path)
    if bd:
        for i in range(len(bd)):
            if bd[i][primary_key[0]] == record_model[primary_key[0]]:
                bd[i] = record_model
                if bd_data_save(bd_path, bd):
                    return record_model[primary_key[0]]
                else:
                    print(f'Ошибка записи данных с № {record_model[primary_key[0]]} в БД {bd_path}')
                    return False
        bd.append(record_model)
        if bd_data_save(bd_path, bd):
            return record_model[primary_key[0]]
        else:
            print(f'Ошибка записи данных с № {record_model[primary_key[0]]} в БД {bd_path}')
            return False
    else:
        bd = []
        bd.append(record_model)
        if bd_data_save(bd_path, bd):
            return record_model[primary_key[0]]
        else:
            print(f'Ошибка записи данных с № {record_model[primary_key[0]]} в БД {bd_path}')
            return False