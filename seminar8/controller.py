import model_department
import model_job
import model_person
import model_company
import view
import menu
import sys
import export_bd
import model_relation

def programm_exit():
    sys.exit()

def person_menu_exit():
    view.view_menu(menu.menu_main)

def  choice_person():
    while True:
        view.view_menu('Сотрудники', menu.menu_person)
        try:
            choice_main = int(input('Введите номер пункта меню: '))
        except:
            print('Введено не целое число')
        else:
            if choice_main == 1:
                model_person.person_add()
            elif choice_main == 2:
                try:
                    id = int(input('Введите номер сотрудника: '))
                except:
                    print('Введено не целое число')
                else:
                    model_person.person_change(id)
            elif choice_main == 3:
                try:
                    id = int(input('Введите номер сотрудника: '))
                except:
                    print('Введено не целое число')
                else:
                    model_person.person_del(id)
            elif choice_main == 4:
                model_person.person_view_list()
            elif choice_main == 5:
                last_name = input('Введите фамилию сотрудника: ')
                model_person.person_search_last_name(last_name)
            elif choice_main == 6:
                model_person.person_view_all()
            elif choice_main == 7:
                prog_run()
            else:
                print('Пункт меню указан неверно')

def choice_sprav():
    while True:
        view.view_menu('Справочники', menu.menu_sprav)
        try:
            choice_main = int(input('Введите номер пункта меню: '))
        except:
            print('Введено не целое число')
        else:
            if choice_main == 1:
                choice_sprav_job()
            elif choice_main == 2:
                choice_sprav_department()
            elif choice_main == 3:
                choice_sprav_company()
            elif choice_main == 4:
                prog_run()
            else:
                print('Пункт меню указан неверно')

def choice_sprav_job():
    while True:
        view.view_menu('Справочник Должностей', menu.menu_sprav_job)
        try:
            choice_main = int(input('Введите номер пункта меню: '))
        except:
            print('Введено не целое число')
        else:
            if choice_main == 1:
                model_job.job_view_list()
            elif choice_main == 2:
                model_job.job_add()
            elif choice_main == 3:
                try:
                    id = int(input('Введите номер должности: '))
                except:
                    print('Введено не целое число')
                else:
                    model_job.job_change(id)
            elif choice_main == 4:
                choice_sprav()
            else:
                print('Пункт меню указан неверно')

def choice_sprav_department():
    while True:
        view.view_menu('Справочник Подразделений', menu.menu_sprav_department)
        try:
            choice_main = int(input('Введите номер пункта меню: '))
        except:
            print('Введено не целое число')
        else:
            if choice_main == 1:
                model_department.department_view_list()
            elif choice_main == 2:
                model_department.department_add()
            elif choice_main == 3:
                try:
                    id = int(input('Введите номер подразделения: '))
                except:
                    print('Введено не целое число')
                else:
                    model_department.department_change(id)
            elif choice_main == 4:
                choice_sprav()
            else:
                print('Пункт меню указан неверно')

def choice_sprav_company():
    while True:
        view.view_menu('Справочник Компаний', menu.menu_sprav_company)
        try:
            choice_main = int(input('Введите номер пункта меню: '))
        except:
            print('Введено не целое число')
        else:
            if choice_main == 1:
                model_company.company_view_list()
            elif choice_main == 2:
                model_company.company_add()
            elif choice_main == 3:
                choice_sprav()
            else:
                print('Пункт меню указан неверно')

def choice_export():
    while True:
        view.view_menu('Экспорт БД', menu.menu_export)
        try:
            choice_main = int(input('Введите номер пункта меню: '))
        except:
            print('Введено не целое число')
        else:
            if choice_main == 1:
                export_bd.export_csv(model_person.bd_path,model_person.model_record,'./export/person.csv')
            elif choice_main == 2:
                export_bd.export_csv(model_company.bd_path, model_company.model_record, './export/company.csv')
            elif choice_main == 3:
                export_bd.export_csv(model_department.bd_path, model_department.model_record, './export/department.csv')
            elif choice_main == 4:
                export_bd.export_csv(model_job.bd_path, model_job.model_record, './export/job.csv')
            elif choice_main == 5:
                (model_record, bd_data) = model_relation.relation_person_all()
                export_bd.export_svod_csv(bd_data, model_record, './export/person_svod.csv')
            elif choice_main == 6:
                prog_run()
            else:
                print('Пункт меню указан неверно')

def prog_run():
    while True:
        view.view_menu('Главное меню', menu.menu_main)
        try:
            choice_main = int(input('Введите номер пункта меню: '))
        except:
            print('Введено не целое число')
        else:
            if choice_main == 1:
                choice_person()
            elif choice_main == 2:
                choice_sprav()
            elif choice_main == 3:
                choice_export()
            elif choice_main == 4:
                programm_exit()
            else:
                print('Пункт меню указан неверно')