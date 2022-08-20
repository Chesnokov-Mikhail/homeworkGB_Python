import model_relation
import common_function
import view

# Путь к БД
bd_path = './bd/person.json'

# наименование ключевого поля, текущее значение ключа
primary_key = ['id',0]

# Структура данных Сотрудника в БД. имя поля: (функция проверки формата, наименование, длина поля, функция получения значения поля)
model_record = {'id':(common_function.int_len,'номер сотрудника', 11,'№', common_function.primary_get_id),
               'last_name': (common_function.str_len,'фамилия', 40, 'фамилия'),
               'name': (common_function.str_len,'имя', 40,'имя'),
               'midle_name': (common_function.str_len,'отчество', 40,'отчество'),
               'birthday': (common_function.date,'дата рождения (формат, dd.mm.yyyy)', 10, 'Д.Р.'),
               'phone': (common_function.phone,'контактный телефон (цифры)', 11,'телефон')}

'''
добавить нового сотрудника
'''
def person_add():
    id = common_function.record_add(bd_path, model_record, primary_key)
    if id:
        print(f'Сотрудник добавлен, ему присвоен номер {id}')
        if model_relation.relation_add(id):
            print(f'Сотрудник принят на должность в подразделение компании')
            return id
        else:
            print(f'Сотрудник не принят на должность в подразделение компании')
            return False
    else:
        print(f'Сотрудник НЕ добавлен')
        return False

'''
Изменение данных сотрудника в БД по его id
'''
def person_change(id):
    if common_function.record_change(id, bd_path, model_record, primary_key):
        print(f'Данные сотрудника с № {id} изменены в БД')
        if model_relation.relation_change(id):
            print(f'Сотруднику изменены должность или подразделение или компания')
            return True
        else:
            print(f'Сотруднику не изменены должность или подразделение или компания')
            return False
    else:
        print(f'Данные сотрудника с № {id} НЕ изменены в БД')
        return False

'''
Удаление сотрудника с id из БД
'''
def person_del(id):
    if common_function.record_del(id, bd_path, primary_key):
        print(f'Данные сотрудника с № {id} удалены в БД')
        if model_relation.relation_del(id):
            return True
        else:
            return False
    else:
        print(f'Данные сотрудника с № {id} НЕ удалены в БД')
        return False

'''
Поиск сотрудника по фамилии в БД. Возвращает запись.
'''
def person_search_last_name(last_name):
    bd_person = common_function.bd_load(bd_path)
    try:
        for i in range(len(bd_person)):
            if bd_person[i]['last_name'] == last_name:
                return view.view_data_str(bd_person[i],model_record)
    except:
        print('Ошибка чтения данных БД')
        return False
    else:
        print(f'Сотрудник с фамилией {last_name} не найден')
        return False

'''
Выводит список всех сотрудников
'''
def person_view_list():
    view.view_bd_load(bd_path,model_record)

'''
Выводит список всех сотрудников с должностями, подразделениями
'''
def person_view_all():
    (model_record, bd_data) = model_relation.relation_person_all()
    view.view_bd(bd_data, model_record)

'''
Получить запись нового или существующего сотрудника для работы с ней в Телеграм
'''
def person_get_record(id=None):
    if id:
        return common_function.record_get_id(id, bd_path, primary_key)
    else:
        return dict.fromkeys(model_record.keys())
