import common_function
import view

# Путь к БД
bd_path = './bd/department.json'

# наименование ключевого поля, текущее значение ключа
primary_key = ['id',0]

# Структура данных Подразделения в БД. имя поля: (функция проверки формата, наименование, длина поля, функция получения значения поля)
model_record = {'id':(common_function.int_len,'номер подразделения', 11,'№', common_function.primary_get_id),
               'department_name': (common_function.str_len,'Наименование подразделения', 20,'Подразделение')}

'''
добавить новое подразделение
'''
def department_add():
    id = common_function.record_add(bd_path, model_record, primary_key)
    if id:
        print(f'Подразделение добавлено, ему присвоен номер {id}')
        return id
    else:
        print(f'Подразделение НЕ добавлено')
        return False

'''
Изменение данных подразделения в БД по его id
'''
def department_change(id):
    if common_function.record_change(id, bd_path, model_record, primary_key):
        print(f'Данные подразделения с № {id} изменены в БД')
        return True
    else:
        print(f'Данные подразделения с № {id} НЕ изменены в БД')
        return False
'''
Удаление подразделения с id из БД
'''
def department_del(id):
    if common_function.record_del(id, bd_path, primary_key):
        print(f'Данные подразделения с № {id} удалены в БД')
        return True
    else:
        print(f'Данные подразделения с № {id} НЕ удалены в БД')
        return False

'''
Выводит список всех подразделений
'''
def department_view_list():
    view.view_bd_load(bd_path,model_record)