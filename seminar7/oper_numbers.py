import cmath
import math
import loger

@loger.loger_oper
def sum(a,b):
    return a+b

@loger.loger_oper
def minus(a,b):
    return a-b

@loger.loger_oper
def multiplication(a,b):
    return a*b

@loger.loger_oper
def division(a,b):
    try:
        return a/b
    # Ошибка деления на ноль
    except ZeroDivisionError:
        return 'Error'

@loger.loger_oper
def modul(a):
    return abs(a)

@loger.loger_oper
def sqrt(a):
    if type(a) == complex:
        return cmath.sqrt(a)
    else:
        return math.sqrt(a)

@loger.loger_oper
def exponentiation(a,b):
    return math.pow(a,b)

@loger.loger_oper
def integer_division(a,b):
    try:
        return a//b
    # Ошибка деления на ноль
    except ZeroDivisionError:
        return 'Error'

@loger.loger_oper
def remain_division(a,b):
    try:
        return a%b
    # Ошибка деления на ноль
    except ZeroDivisionError:
        return 'Error'