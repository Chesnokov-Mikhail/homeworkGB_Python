from functools import wraps
import datetime as dt
import os.path

# функция декоратор для логирования операций
def loger_oper(func):
    file_path_log = 'log.txt'
    if not os.path.exists(file_path_log):
        with open(file_path_log, 'w') as fw:
            fw.write('Date and time operation; Operation; Arguments; Result \n')
    @wraps(func)
    def wrapper(*argv):
        with open(file_path_log, 'a') as fa:
            result = func(*argv)
            arg_str = ', '.join(repr(arg) for arg in argv)
            oper_name = func.__name__
            log_text = '; '.join([dt.datetime.today().strftime('%d.%m.%Y %H:%M:%S'), oper_name,arg_str, str(result)]) + '\n'
            fa.write(log_text)
        return result
    return wrapper