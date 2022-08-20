import common_function
import main
import model_department
import model_job
import model_person
import model_company
import view
import menu
import sys
import export_bd
import model_relation

#Переменная для определения в каком меню находится пользователь
menu_select = menu.menu_main

#Переменная для определения с какой моделью данных работает пользователь
model_select = None

#Генератор для определения с какое поле из модели данных работает пользователь
key_model_select = None

#Переменная для определения с какое поле из модели данных работает пользователь
key_model = None

#Переменная для хранения новой/изменяемой запис модели данных, с которой работает пользователь
record_model = None

#Переменная для хранения пути к БД модели данных, с которой работает пользователь
bd_path = ''

#Переменная для хранения пути к примари кей БД модели данных, с которой работает пользователь
primary_key = None

#Переменная для хранения модели данных поля записи в связной таблицы БД
model_record_rel_select = None

#Переменная для хранения информации когда выбрана операция удаления
action_delete = False

#Переменная для определения запуска
start_prog = False

def programm_exit():
    global start_prog
    start_prog = False
    print('Выход из программы.')
    sys.exit()

def choice_person():
    global menu_select
    view.view_menu('Сотрудники', menu.menu_person)
    print('Введите номер пункта меню: ')
    menu_select = menu.menu_person

def choice_sprav():
    global menu_select
    view.view_menu('Справочники', menu.menu_sprav)
    print('Введите номер пункта меню: ')
    menu_select = menu.menu_sprav

def choice_sprav_job():
    global menu_select
    view.view_menu('Справочник Должностей', menu.menu_sprav_job)
    print('Введите номер пункта меню: ')
    menu_select = menu.menu_sprav_job

def choice_sprav_department():
    global menu_select
    view.view_menu('Справочник Подразделений', menu.menu_sprav_department)
    print('Введите номер пункта меню: ')
    menu_select = menu.menu_sprav_department

def choice_sprav_company():
    global menu_select
    view.view_menu('Справочник Компаний', menu.menu_sprav_company)
    print('Введите номер пункта меню: ')
    menu_select = menu.menu_sprav_company

def choice_export():
    global menu_select
    view.view_menu('Экспорт БД', menu.menu_export)
    print('Введите номер пункта меню: ')
    menu_select = menu.menu_export

def prog_run():
    global menu_select
    global start_prog
    global model_select
    global record_model
    global key_model_select
    view.view_menu('Главное меню', menu.menu_main)
    print('Введите номер пункта меню: ')
    menu_select = menu.menu_main
    start_prog = True
    init_var_prog()

def init_var_prog():
    global model_select
    global record_model
    global key_model_select
    global key_model
    global bd_path
    global primary_key
    global model_record_rel_select
    global action_delete
    model_select = None
    record_model = None
    key_model_select = None
    key_model = None
    bd_path = ''
    primary_key = None
    model_record_rel_select = None
    action_delete = False

# '''
# Получение поля из модели для запроса пользователя для его заполнения
# '''
# def telegram_get_field_model(update, context, model_select, record_model, path, p_key):
#     global key_model_select
#     global key_model
#     global bd_path
#     global primary_key
#
#     bd_path = path
#     primary_key = p_key
#     if key_model_select:
#         try:
#             key_model = next(key_model_select)
#             main.question_field_model(update, context, model_select, key_model)
#         # Если поля в модели закончились то сохраняем запись в БД
#         except StopIteration as e:
#             telegram_save_record_model(update, context, model_select, record_model, path, p_key)
#     else:
#         key_model_select = common_function.get_field_model(record_model, path, model_select, p_key)
#         key_model = next(key_model_select)
#         main.question_field_model(update, context, model_select, key_model)

'''
Получение поля из модели для запроса пользователя в Телеграм для его заполнения 
'''
def telegram_get_field_model(update, context, model_select, record_model, path, p_key):
    global key_model_select
    global key_model
    global bd_path
    global primary_key
    global model_record_rel_select

    bd_path = path
    primary_key = p_key
    if key_model_select:
        try:
            key_model = next(key_model_select)
            # Обработка модели связной таблицы
            if model_select == model_relation.model_record:
                if model_select[key_model][4] == model_person:
                    telegram_get_field_model(update, context, model_select, record_model, path, p_key)
                    return
                if model_select[key_model][4] == model_company:
                    output = model_company.company_view_list_str()
                elif model_select[key_model][4] == model_department:
                    output = model_department.department_view_list_str()
                elif model_select[key_model][4] == model_job:
                    output = model_job.job_view_list_str()
                else:
                    output = ''
                model_record_rel_select = model_select[key_model][4].model_record
                val_key = record_model[key_model]
                # Вывод справочника перед выбором значения
                main.view_question_data(update, context, output)
                # Запрос значения из справочника
                main.question_id_record_rel_model(update, context, model_select, key_model, val_key)
            else:
                main.question_field_model(update, context, model_select, key_model)
        # Если поля в модели закончились то сохраняем запись в БД
        except StopIteration as e:
            telegram_save_record_model(update, context, model_select, record_model, path, p_key)
    else:
        key_model_select = common_function.get_field_model(record_model, path, model_select, p_key)
        key_model = next(key_model_select)
        # Обработка модели связной таблицы
        if model_select == model_relation.model_record:
            if model_select[key_model][4] == model_person:
                telegram_get_field_model(update, context, model_select, record_model, path, p_key)
                return
            if model_select[key_model][4] == model_company:
                output = model_company.company_view_list_str()
            elif model_select[key_model][4] == model_department:
                output = model_department.department_view_list_str()
            elif model_select[key_model][4] == model_job:
                output = model_job.job_view_list_str()
            else:
                output = ''
            model_record_rel_select = model_select[key_model][4].model_record
            val_key = record_model[key_model]
            # Вывод справочника перед выбором значения
            main.view_question_data(update, context, output)
            # Запрос значения из справочника
            main.question_id_record_rel_model(update, context, model_select, key_model, val_key)
        else:
            main.question_field_model(update, context, model_select, key_model)

'''
Сохранение введенных данных в БД из Телеграм
'''
def telegram_save_record_model(update, context, model_select, record_model, path, p_key):
    id = common_function.record_save_telegram(record_model, path, p_key)
    main.answer_save_model(update, context, id)
    # Обрабатываем связные таблицы для person
    if model_select == model_person.model_record:
        init_var_prog()
        relation_set(update, context, id)
    else:
        init_var_prog()

'''
Заполнение модели связных таблиц
'''
def relation_set(update, context, id):
    global model_select
    global record_model

    # Получение записи в связной таблице по id person
    record_model = model_relation.relation_get_record_person(id)
    if record_model:
        model_select = model_relation.model_record
        telegram_get_field_model(update, context, model_select, record_model, model_relation.bd_path,
                                 model_relation.primary_key)
    else:
        print('Ошибка ввода данных в связные таблицы')

'''
Получение записи модели по введенному пользователю идентификатору в Телеграм
'''
def get_record_model(update, context, model_select, record_modely, path, p_key):
    global record_model
    global action_delete

    if model_select == model_department:
        record_model = model_department.department_get_record(record_modely[p_key[0]])
    elif model_select == model_job:
        record_model = model_job.job_get_record(record_modely[p_key[0]])
    elif model_select == model_company:
        record_model = model_company.company_get_record(record_modely[p_key[0]])
    elif model_select == model_person:
        record_model = model_person.person_get_record(record_modely[p_key[0]])
    # Если запись найдена, то проходим по всем полям медели для возможности изменения
    if record_model and not action_delete:
        telegram_get_field_model(update, context, model_select, record_model, path, p_key)
    elif record_model and action_delete:
        model_person.person_del(record_modely[p_key[0]])

'''
Запрос идентификатора изменяемой/удаляемых записи модели в Телеграм
'''
def change_record_model(update, context, model_select, record_model, path, p_key):
    global key_model
    global bd_path
    global primary_key

    bd_path = path
    primary_key = p_key
    key_model = p_key[0]
    main.question_id_record_model(update, context, model_select, key_model)

'''
Запрос поиска записи модели в Телеграм
'''
def search_record_model(update, context, model_select, record_model, path, p_key):
    global key_model
    global bd_path
    global primary_key

    bd_path = path
    primary_key = p_key
    key_model = 'last_name'
    main.question_search_record_model(update, context, model_select, key_model)

'''
Результат поиска записи модели для Телеграм
'''
def view_search_record_model(update, context, model_select, record_model, path, p_key, search_val):
    main.answer_document_data(update, context, model_person.person_search_last_name(search_val))
'''
Функция выбора действия при выборе пунктов меню
'''
def choice_menu(choice_main, update, context):
    global menu_select
    global model_select
    global record_model
    global action_delete

    if choice_main == -1:
        menu_select = menu.menu_main
        prog_run()
    if menu_select == menu.menu_main:
        if choice_main == 1:
            choice_person()
        elif choice_main == 2:
            choice_sprav()
        elif choice_main == 3:
            choice_export()
        elif choice_main == 4:
            programm_exit()
    elif menu_select == menu.menu_export:
        if choice_main == 1:
            export_bd.export_csv(model_person.bd_path, model_person.model_record, './export/person.csv')
            return './export/person.csv'
        elif choice_main == 2:
            export_bd.export_csv(model_company.bd_path, model_company.model_record, './export/company.csv')
            return './export/company.csv'
        elif choice_main == 3:
            export_bd.export_csv(model_department.bd_path, model_department.model_record, './export/department.csv')
            return './export/department.csv'
        elif choice_main == 4:
            export_bd.export_csv(model_job.bd_path, model_job.model_record, './export/job.csv')
            return './export/job.csv'
        elif choice_main == 5:
            (model_record, bd_data) = model_relation.relation_person_all()
            export_bd.export_svod_csv(bd_data, model_record, './export/person_svod.csv')
            return './export/person_svod.csv'
        elif choice_main == 6:
            prog_run()
    elif menu_select == menu.menu_sprav_company:
        if choice_main == 1:
            model_company.company_view_list()
        elif choice_main == 2:
            init_var_prog()
            model_select = model_company.model_record
            record_model = model_company.company_get_record()
            telegram_get_field_model(update, context, model_select, record_model, model_company.bd_path, model_company.primary_key)
        elif choice_main == 3:
            init_var_prog()
            choice_sprav()
    elif menu_select == menu.menu_sprav_department:
        if choice_main == 1:
            model_department.department_view_list()
        elif choice_main == 2:
            init_var_prog()
            model_select = model_department.model_record
            record_model = model_department.department_get_record()
            telegram_get_field_model(update, context, model_select, record_model, model_department.bd_path,
                                     model_department.primary_key)
        elif choice_main == 3:
            init_var_prog()
            model_select = model_department.model_record
            record_model = model_department.department_get_record()
            change_record_model(update, context, model_select, record_model, model_department.bd_path, model_department.primary_key)
        elif choice_main == 4:
            init_var_prog()
            choice_sprav()
    elif menu_select == menu.menu_sprav_job:
        if choice_main == 1:
            model_job.job_view_list()
        elif choice_main == 2:
            init_var_prog()
            model_select = model_job.model_record
            record_model = model_job.job_get_record()
            telegram_get_field_model(update, context, model_select, record_model, model_job.bd_path,
                                     model_job.primary_key)
        elif choice_main == 3:
            init_var_prog()
            model_select = model_job.model_record
            record_model = model_job.job_get_record()
            change_record_model(update, context, model_select, record_model, model_job.bd_path,
                                model_job.primary_key)
        elif choice_main == 4:
            init_var_prog()
            choice_sprav()
    elif menu_select == menu.menu_sprav:
        if choice_main == 1:
            choice_sprav_job()
        elif choice_main == 2:
            choice_sprav_department()
        elif choice_main == 3:
            choice_sprav_company()
        elif choice_main == 4:
            prog_run()
    elif menu_select == menu.menu_person:
        if choice_main == 1:
            init_var_prog()
            model_select = model_person.model_record
            record_model = model_person.person_get_record()
            telegram_get_field_model(update, context, model_select, record_model, model_person.bd_path,
                                     model_person.primary_key)
        elif choice_main == 2:
            init_var_prog()
            model_select = model_person.model_record
            record_model = model_person.person_get_record()
            change_record_model(update, context, model_select, record_model, model_person.bd_path,
                                model_person.primary_key)
        elif choice_main == 3:
            init_var_prog()
            model_select = model_person.model_record
            record_model = model_person.person_get_record()
            action_delete = True
            change_record_model(update, context, model_select, record_model, model_person.bd_path,
                                model_person.primary_key)
#            model_person.person_del(id)
        elif choice_main == 4:
            export_bd.export_csv(model_person.bd_path, model_person.model_record, './export/person.csv')
            return './export/person.csv'
            #model_person.person_view_list()
        elif choice_main == 5:
            init_var_prog()
            model_select = model_person.model_record
            search_record_model(update, context, model_select, record_model, model_person.bd_path,
                                model_person.primary_key)
# В телеграмм не получится вывести в message текст отчета, поэтому оставлен вариант его экспорта
#        elif choice_main == 6:
#            model_person.person_view_all()
        elif choice_main == 6:
            init_var_prog()
            prog_run()
    else:
        print('Пункт меню указан неверно')
