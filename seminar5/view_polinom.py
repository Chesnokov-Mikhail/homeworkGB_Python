def GenerateTerms(degree: int, sign: str, coef: int, var: int) -> str:
    if degree == 0:
        return f'{sign} {var}'
    elif degree == 1:
        if coef == 1:
            return f'{sign} x'
        else:
            return f'{sign} {coef}*x'
    else:
        if coef == 1:
            return f'{sign} x^{degree}'
        else:
            return f'{sign} {coef}*x^{degree}'


def view_poli(dict_polinom: dict):
    # {degree: [sign, coeficient, var]}
    result = ''
    for (i, degree) in enumerate(sorted(dict_polinom.keys(), reverse=True)):
        if i == 0 and dict_polinom[degree][0] == '+':
            result += GenerateTerms(degree, '', dict_polinom[degree][1], dict_polinom[degree][2])
        else:
            result += ' ' + GenerateTerms(degree, *dict_polinom[degree])
    return result