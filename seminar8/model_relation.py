import common_function
import model_person
import model_company
import model_job
import model_department

# Путь к БД
import view

bd_path = './bd/relation.json'

# наименование ключевого поля, текущее значение ключа
primary_key = ['id',0]

# Структура данных связной таблицы отношений в БД. имя поля: (функция проверки формата, наименование, длина поля, функция получения значения поля)
model_record = {'id':(common_function.int_len,'номер связи', 11,'№', common_function.primary_get_id),
                'id_company':(common_function.int_len,'номер компании', 11,'№ компании', model_company),
                'id_person':(common_function.int_len,'номер сотрудника', 11,'№ сотрудника', model_person),
                'id_department':(common_function.int_len,'номер подразделения', 11,'№ подразделения', model_department),
                'id_job':(common_function.int_len,'номер должности', 11,'№ должности', model_job)}

'''
Добавляем связи между таблицами при добавлении сотрудника
'''
def relation_add(id_person):
    record_new = dict.fromkeys(model_record.keys())
    try:
        for key_field, field_value in model_record.items():
            if key_field == primary_key[0]:
                record_new[key_field] = field_value[0](field_value[4](bd_path, primary_key), field_value[2]) + 1
            elif key_field == 'id_person':
                record_new[key_field] = id_person
            else:
                bd_key = common_function.bd_load(field_value[4].bd_path)
                # Отображаем справочник перед выбором номера из него
                view.view_bd(bd_key, field_value[4].model_record)
                record_new[key_field] = field_value[0](input(f'Введите {field_value[1]}: '),field_value[2])
                # Проверяем правильность указания id из справочника bd_key
                for i in range(0,len(bd_key)):
                    if record_new[key_field] == bd_key[i][field_value[4].primary_key[0]]:
                        break
                    elif i == len(bd_key) - 1:
                        raise
    except:
        print('Ошибка в формате данных. Новые данные не сохранены.')
        return False
    else:
        if common_function.bd_data_add(bd_path,record_new):
            common_function.primary_set_id(primary_key, record_new[primary_key[0]])
            return record_new[primary_key[0]]
        else:
            print(f'Ошибка добавления новой записи в БД {bd_path}')
            return False

'''
Изменение связи между таблицами при изменении данных сотрудника
'''
def relation_change(id_person):
    record_index = -1
    bd_record = common_function.bd_load(bd_path)
    if bd_record:
        try:
            for i in range(len(bd_record)):
                if bd_record[i]['id_person'] == id_person:
                    record_index = i
                    break
        except:
            print(f'Ошибка чтения данных записи с № {id_person} в связной БД {bd_path}')
            return False
    else:
        print(f'Связная БД {bd_path} пуста')
    # Если запись в связной таблице найдена, то такую запись можем изменить
    if record_index != -1:
        view.view_data(bd_record[record_index], model_record)
        try:
            for key_field, field_value in model_record.items():
                if key_field == primary_key[0]:
                    continue
                else:
                    bd_key = common_function.bd_load(field_value[4].bd_path)
                    # Отображаем справочник перед выбором номера из него
                    view.view_bd(bd_key, field_value[4].model_record)
                    new_value = input(
                        f'При необходимости измените текущее значение {bd_record[record_index][key_field]}: ')
                    # если изменения есть, то проверяем формат и правильность указания id из справочника bd_key, сохраняем в списке
                    if new_value:
                        bd_record[record_index][key_field] = field_value[0](new_value, field_value[2])
                        for j in range(len(bd_key)):
                            if bd_record[record_index][key_field] == bd_key[j][field_value[4].primary_key[0]]:
                                break
                            elif j == len(bd_key) - 1:
                                raise
        except:
            print(f'Ошибка в формате измененных данных. Данные записи не изменены в связной БД {bd_path}.')
        else:
            if common_function.bd_data_save(bd_path, bd_record):
                return True
            else:
                print(f'Ошибка изменения данных записи в связной БД {bd_path}.')
                return False
    # Если записи в связной таблице нет, то добавляем такую запись
    else:
        print(f'Запись с № {id_person} не найдена в связной БД {bd_path}.')
        if relation_add(id_person):
            return True
        else:
            return False

'''
Удаление связи между таблицами при удалении сотрудника
'''
def relation_del(id_person):
    db_record = common_function.bd_load(bd_path)
    try:
        if db_record:
            for i in range(len(db_record)):
                if db_record[i]['id_person'] == id_person:
                    db_record.remove(db_record[i])
                    if common_function.bd_data_save(bd_path, db_record):
                        print(f'Данные записи с № {id} удалены из БД {bd_path}')
                        return True
                    else:
                        raise
        else:
            print(f'Связная БД {bd_path} пуста')
            return True
    except:
        print(f'Ошибка при удаления записи о сотруднике с № {id_person} в связной БД {bd_path}')
        return False
    else:
        print(f'Запись о сотруднике с № {id_person} не найдена в связной БД {bd_path}')
        return False

'''
Строим сводную таблицу по сотрудникам и связанным с ними таблицами
'''
def relation_person_all():
    db_person = common_function.bd_load(model_person.bd_path)
    db_relation = common_function.bd_load(bd_path)
    db_person_all = []
    for person in db_person:
        rel_record = dict.fromkeys(model_record.keys())
        for rel in db_relation:
            if rel['id_person'] == person['id']:
                rel_record = rel
                break
        for key_field, field_value in model_record.items():
            if key_field == primary_key[0] or key_field == 'id_person':
                continue
            elif rel_record[key_field]:
                # Получаем запись связной таблицы, связанной с данной записью person
                record_key = common_function.record_get_id(rel_record[key_field], field_value[4].bd_path, field_value[4].primary_key)
                # Удаляем значение ключа "id" записи звязных таблиц, чтобы потом добавить оставшиеся значения в итоговую таблицу
                value_primary_key = record_key.pop(field_value[4].primary_key[0])
                person.update(record_key)
            else:
                # Получаем пустую запись из модеи связной таблицы, не связанной с данной записью person
                record_key = dict.fromkeys(field_value[4].model_record.keys())
                # Удаляем значение ключа "id" записи звязных таблиц, чтобы потом добавить оставшиеся значения в итоговую таблицу
                value_primary_key = record_key.pop(field_value[4].primary_key[0])
                person.update(record_key)
        db_person_all.append(person)
    # Собираем итоговую модель связанных таблиц для печати и экспорта
    model_record_all = {}
    model_record_all.update(model_person.model_record)
    for key_field, field_value in model_record.items():
        if key_field == primary_key[0] or key_field == 'id_person':
            continue
        model_record_key = field_value[4].model_record.copy()
        value_primary_key = model_record_key.pop(field_value[4].primary_key[0])
        model_record_all.update(model_record_key)
    return (model_record_all, db_person_all)