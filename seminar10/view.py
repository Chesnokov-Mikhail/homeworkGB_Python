import common_function

'''
Отображение меню
'''
def view_menu(caption, menu):
    print(f'{caption}')
    print(f'{"":-<30}')
    for key, value in menu.items():
        print(f'{key}. {value}')
    print(f'{"":-<30}')
#    print('\n')

'''
Отображение записи из таблицы БД
'''
def view_data(data, model_record):
    for key_field, field_value in model_record.items():
        print(f'|{field_value[3]:_^{field_value[2]}}', end='')
    print('|')
    for key, value in data.items():
        if value == None:
            value = ''
        print(f'|{value: ^{model_record[key][2]}}', end='')
    print('|')
    print('')

'''
Отображение записи из таблицы БД в строку
'''
def view_data_str(data, model_record):
    result = ''
    for key_field, field_value in model_record.items():
        result += f'|{field_value[3]:_^{field_value[2]}}'
    result +='| \n'
    for key, value in data.items():
        if value == None:
            value = ''
        result += f'|{value: ^{model_record[key][2]}}'
    result +='| \n'
    return result

'''
Отображение таблицы БД с загрузкой из bd_path
'''
def view_bd_load(bd_path, model_record):
    bd_data = common_function.bd_load(bd_path)
    if bd_data:
        view_bd(bd_data, model_record)
    else:
        print(f'В {bd_path} нет записей для отображения')

'''
Отображение таблицы БД bd_data
'''
def view_bd(bd_data, model_record):
    for key_field, field_value in model_record.items():
        print(f'|{field_value[3]:_^{field_value[2]}}', end='')
    print('|')
    for record in bd_data:
        for key, value in record.items():
            if value == None:
                value = ''
            print(f'|{value: ^{model_record[key][2]}}', end='')
        print('|')
    print('')

'''
Отображение таблицы БД bd_data в строку (для небольших справочников)
'''
def view_bd_str(bd_data, model_record):
    result = ''
    for key_field, field_value in model_record.items():
        result += f'|{field_value[3]:_^{field_value[2]}}'
    result += '| \n'
    for record in bd_data:
        for key, value in record.items():
            if value == None:
                value = ''
            result += f'|{value: ^{model_record[key][2]}}'
        result += '| \n'
    result += '\n'
    return result
