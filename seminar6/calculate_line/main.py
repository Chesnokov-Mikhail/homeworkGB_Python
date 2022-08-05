'''
Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,.
приоритет операций стандартный.
*Пример:
2+2 => 4;
1+2*3 => 7;
1-2*3 => -5;
- Добавьте возможность использования скобок, меняющих приоритет операций.
Пример:
1+2*3 => 7;
(1+2)*3 => 9;
'''
import input_line
import analysis_line as al

if __name__ == "__main__":
    line = input_line.user_input()
    if line:
        try:
            sp_line = al.parse_line(line)
            print('{} => {}'.format(line, al.sequence_create(sp_line)))
        except:
            print('Ошибка вычисления')
    else:
        print('Не введено арифметическое выражение')