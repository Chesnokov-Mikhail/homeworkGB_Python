def parse_line(line):
    sp_new = []
    sp_op = ['+','-','*','/','(',')']
    num = ''
    # удаляем все пробелы в выражении
    new_line = "".join(line.split())
    for s in new_line:
        if s in sp_op:
            if num:
                try:
                    sp_new.append(float(num))
                except:
                    print('Ошибка. В арифметическом выражении указаны не числовые значения')
                    return []
                num = ''
            sp_new.append(s)
        else:
            num += s
    if num:
        try:
            sp_new.append(float(num))
        except:
            print('Ошибка. В арифметическом выражении указаны не числовые значения')
            return []
    return sp_new

def op_run(x, oper, y):
    if oper == "*":
        result = x * y
    if oper == "/":
        result = x / y
    if oper == "+":
        result = x + y
    if oper == "-":
        result = x - y
    return result

# Находим ()
def find_bkt(sp):
    size = len(sp)
    sp_tuple_bkt = []
    sp_index_open = []
    sp_index_close = []
    start = 0
    stop = size
    while True:
        try:
            start = sp.index('(', start, stop)
            sp_index_open.append(start)
            start += 1
        except:
            break
    start = 0
    while True:
        try:
            start = sp.index(')', start, stop)
            sp_index_close.append(start)
            start += 1
        except:
            break
    if len(sp_index_open) != 0:
        if len(sp_index_close) != len(sp_index_open):
            print('Количество открывающихся скобок не совпадает с количеством закрывающихся скобок')
            raise
        sp_index_open.reverse()
        for i in sp_index_close:
            for j in sp_index_open:
                if i > j:
                    sp_tuple_bkt.append((j, i))
                    break
    return sp_tuple_bkt

def sequence_oper(sp_bkt):
    sp_other = []
    s_last = ''
    res = 0
    for i, s in enumerate(sp_bkt):
        if s in ['*', '/']:
            if s_last in ['*', '/']:
                res = op_run(sp_other[-1], s, sp_bkt[i + 1])
                sp_other[-1] = res
            else:
                res = op_run(sp_bkt[i - 1], s, sp_bkt[i + 1])
                sp_other[-1] = res
            s_last = s
        elif s in ['+', '-']:
            sp_other.append(s)
            s_last = s
        else:
            if s_last not in ['*', '/']:
                sp_other.append(s)
    res = 0
    s_last = ''
    for i, s in enumerate(sp_other):
        if s in ['+', '-']:
            res = op_run(res, s, sp_other[i + 1])
            s_last = s
        else:
            if s_last not in ['+', '-']:
                res = sp_other[i]
    return res

def sequence_create(sp):
    bkt = find_bkt(sp)
    sp_new = []
    size = len(sp)
    start = 0
    for (i,j) in bkt:
        if start < i:
            sp_new.extend(sp[start:i])
        rezult = sequence_oper(sp[i+1:j])
        sp_new.append(rezult)
        start = (j + 1) if (j + 1) < size else j
    if start < size:
        sp_new.extend(sp[start:size])
    return sequence_oper(sp_new)
