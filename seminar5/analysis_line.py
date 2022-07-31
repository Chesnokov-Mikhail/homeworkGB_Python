def analysis_polinom(line):
    sp_new = []
    if len(line) != 0:
        sp = [x.strip() for x in line.partition('-') if x.strip() != '']
        for i in range(0, line.count('-') - 1):
            sp.extend([x.strip() for x in sp.pop().partition('-') if x.strip() != ''])
        for (i, s) in enumerate(sp):
            if s != '-':
                sp_plus = [x.strip() for x in s.partition('+') if x.strip() != '']
                for j in range(0, s.count('+') - 1):
                    sp_plus.extend([x.strip() for x in sp_plus.pop().partition('+') if x.strip() != ''])
                sp_new.extend(sp_plus)
            else:
                sp_new.append(s)
    return sp_new

def create_dict_polinom(sp):
    # {degree: [sign, coeficient, var]}
    dict_polinom = {}
    for s in sp:
        if s in ('-', '+'):
            sign = s
        else:
            coeficients = [x.strip() for x in s.split('*')]
            if len(coeficients) > 1:
                coeficient = int(coeficients.pop(0))
            else:
                coeficient = 1
            degrees = [x.strip() for x in coeficients[0].split('^')]
            if len(degrees) > 1:
                degree = int(degrees.pop())
                var = 0
            else:
                degree = 1
                var = 0
                if degrees[0].isdigit():
                    degree = 0
                    var = int(degrees[0])
            value_dict = dict_polinom.setdefault(degree, ['+', 0, 0])
            if value_dict[0] != sign:
                if value_dict[1] >= coeficient:
                    value_dict[1] -= coeficient
                else:
                    value_dict[1] = coeficient - value_dict[1]
                    value_dict[0] = sign
                if value_dict[2] >= var:
                    value_dict[2] -= var
                else:
                    value_dict[2] = var - value_dict[2]
                    value_dict[0] = sign
            else:
                value_dict[1] += coeficient
                value_dict[2] += var
    return dict_polinom

def sum_polinom(polinom1, polinom2):
    dict_sum = {}
    # {degree: [sign, coeficient, var]}
    for (key, term1) in polinom1.items():
        term2 = polinom2.pop(key, False)
        if term2:
            if term2[0] == term1[0]:
                if key == 0:
                    dict_sum[key] = [term1[0], 1, term1[2] + term2[2]]
                else:
                    dict_sum[key] = [term1[0], term1[1] + term2[1], term1[2]]
            else:
                if key == 0:
                    if term2[2] >= term1[2]:
                        dict_sum[key] = [term2[0], 1, term2[2] - term1[2]]
                    else:
                        dict_sum[key] = [term1[0], 1, term1[2] - term2[2]]
                else:
                    if term2[1] >= term1[1]:
                        dict_sum[key] = [term2[0], term2[1] - term1[1], term1[2]]
                    else:
                        dict_sum[key] = [term1[0], term1[1] - term2[1], term1[2]]
        else:
            dict_sum[key] = term1
    dict_sum.update(polinom2)
    return dict_sum