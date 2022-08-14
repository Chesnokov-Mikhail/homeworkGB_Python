import csv
import common_function
import os.path

'''
Экспорт таблицы БД bd_path в файл file_patch формат csv
'''
def export_csv(bd_path, model_record, file_patch):
    bd = common_function.bd_load(bd_path)
    if bd:
        with open(file_patch,'w') as fw:
            fw_csv = csv.writer(fw)
            caption = []
            for key_field in model_record.keys():
                caption.append(key_field)
            fw_csv.writerow(caption)
            for item in bd:
                fw_csv.writerow(list(item.values()))
        print('Выполнен экспорт в файл:', os.path.abspath(file_patch))

'''
Экспорт данных bd_data в файл file_patch формат csv
'''
def export_svod_csv(bd_data, model_record, file_patch):
    with open(file_patch,'w') as fw:
        fw_csv = csv.writer(fw)
        caption = []
        for key_field in model_record.keys():
            caption.append(key_field)
        fw_csv.writerow(caption)
        for item in bd_data:
            fw_csv.writerow(list(item.values()))
    print('Выполнен экспорт в файл:', os.path.abspath(file_patch))