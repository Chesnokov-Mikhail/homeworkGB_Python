'''
3* (необзательная).
Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве
используется в этой книге.
Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова,
разделённые пробелом и вывести получившуюся статистику.
Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального
слова в этой строке число его повторений (без учёта регистра) в формате "слово количество"
(см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться только один раз.

Sample Input 1:

a aa abC aa ac abc bcd a
Sample Output 1:
ac 1
a 2
abc 2
bcd 1
aa 2

Sample Input 2:
a A a
Sample Output 2:
a 3
'''

'''
Подсчет количества уникальных слов в тексте.
Вход: текст
Выход: словарь (слово: количество данного слова в тексте)
'''
def count_unique_word_text(text):
    word_dict = {}
    sp = [word.strip(',.{}():;-').lower() for word in text.split()]
    for s in sp:
        count = word_dict.setdefault(s, 0)
        word_dict[s] = count + 1
    return word_dict

'''
Подсчет количества уникальных слов в файле.
Вход: файловый идентификатор
Выход: словарь (слово: количество данного слова в тексте файла)
'''
def count_unique_words_text(ftext):
    word_dict = {}
    for text in ftext:
        sp = [word.strip(',.{}()[]?!"\n\v\'\r:;-').lower() for word in text.split()]
        for s in sp:
            if s != '':
                count = word_dict.setdefault(s, 0)
                word_dict[s] = count + 1
    return word_dict

'''
Печать словаря в виде: ключ - значение 
'''
def print_dict(word_dict):
    for (key, value) in word_dict.items():
        print('{} - {}'.format(key, value))

if __name__ == '__main__':
    line = input('Введите строку для подсчета количества уникальных слов: ')
    print_dict(count_unique_word_text(line))

#    with open('voyna-i-mir-tom-1.txt', 'r', encoding='windows-1251') as fr:
#        print_dict(count_unique_words_text(fr))