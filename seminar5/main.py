'''
Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
Это не просто сумма всех коэффициентов.
Сумма многочленов равна многочлену, членами которого являются все члены данных многочленов.
например, в 1 файле было 3*x^3 + 5*x^2+10*x+11, в другом 7*x^2+55
то в итоге будет, 3*x^3 + 12*x^2+10*x+66
'''
import load_polinom as lp
import analysis_line as al
import view_polinom as view
import save_polinom as save

if __name__ == '__main__':
    str_poli1 = lp.load_from_file('.\polinom1.txt')
    str_poli2 = lp.load_from_file('.\polinom2.txt')
    dict_poli1 = al.create_dict_polinom(al.analysis_polinom(str_poli1))
    dict_poli2 = al.create_dict_polinom(al.analysis_polinom(str_poli2))
    result = view.view_poli(al.sum_polinom(dict_poli1, dict_poli2))
    save.save_to_file('sum_polinom.txt', result)