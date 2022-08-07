'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
'''
import file_work
import rle_algoritm

if __name__ == "__main__":
    data = file_work.load_file('text_for_rle.txt')
    if len(data) != 0:
        compress_data = rle_algoritm.compression_rle(data)
        file_work.save_file('text_rle.txt',compress_data)
    else:
        print('Файл для сжатия пустой')

    data_rle = file_work.load_file('text_rle.txt')
    if len(data_rle) != 0:
        decompres_data = rle_algoritm.recovery_from_rle(data_rle)
        file_work.save_file('text_from_rle.txt', decompres_data)
    else:
        print('Файл для восстановления пустой')