import common_function
import view

# Путь к БД
bd_path = './bd/job.json'

# наименование ключевого поля, текущее значение ключа
primary_key = ['id',0]

# Структура данных Должности в БД. имя поля: (функция проверки формата, наименование, длина поля, функция получения значения поля)
model_record = {'id':(common_function.int_len,'номер должности', 11,'№', common_function.primary_get_id),
               'job_name': (common_function.str_len,'Наименование должности', 20,'Должность')}

'''
добавить новую должность
'''
def job_add():
    id = common_function.record_add(bd_path, model_record, primary_key)
    if id:
        print(f'Должность добавлена, ей присвоен номер {id}')
        return id
    else:
        print(f'Должность НЕ добавлена')
        return False

'''
Изменение данных должности в БД по его id
'''
def job_change(id):
    if common_function.record_change(id, bd_path, model_record, primary_key):
        print(f'Данные должности с № {id} изменены в БД')
        return True
    else:
        print(f'Данные должности с № {id} НЕ изменены в БД')
        return False

'''
Удаление должности с id из БД
'''
def job_del(id):
    if common_function.record_del(id, bd_path, primary_key):
        print(f'Данные дожности с № {id} удалены в БД')
        return True
    else:
        print(f'Данные должности с № {id} НЕ удалены в БД')
        return False

'''
Выводит список всех должностей
'''
def job_view_list():
    view.view_bd_load(bd_path,model_record)