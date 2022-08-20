import csv
import common_function
import os.path
import tempfile

# получаем путь к временной папке в ОС и определяем имя файла
storage_path = os.path.join(tempfile.gettempdir(), 'print.txt')
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
        print('Выполнен экспорт в файл')

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
    print('Выполнен экспорт в файл')

'''
Экспорт данных вывода print в текстовый формат
'''
def export_to_txt(in_data):
    with open(storage_path,'w') as fw:
        fw.write(in_data)
    return storage_path