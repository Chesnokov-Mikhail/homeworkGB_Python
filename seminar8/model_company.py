import common_function
import view

# Путь к БД
bd_path = './bd/company.json'

# наименование ключевого поля, текущее значение ключа
primary_key = ['id',0]

# Структура данных Компании в БД. имя поля: (функция проверки формата, наименование, длина поля, функция получения значения поля)
model_record = {'id':(common_function.int_len,'номер компании', 11,'№', common_function.primary_get_id),
               'company_name': (common_function.str_len,'Наименование организации', 40,'Организация'),}

'''
добавить новую компанию
'''
def company_add():
    id = common_function.record_add(bd_path, model_record, primary_key)
    if id:
        print(f'Организация добавлена, ей присвоен номер {id}')
        return id
    else:
        print(f'Организация НЕ добавлена')
        return False

'''
Выводит список компаний
'''
def company_view_list():
    view.view_bd_load(bd_path,model_record)