# Задание "Раз, два, три, четыре, пять .... Это не всё?":
#
#
# Входные данные (применение функции):
# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# result = calculate_structure_sum(data_structure)
# print(result)
#
# Выходные данные (консоль):
# 99
#
# Примечания (рекомендации):
# Весь подсчёт должен выполняться одним вызовом функции.
# Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
# Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
# Для определения типа данного используйте функцию isinstance.

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_structure_sum(massiv):
    summ = 0

    for i in massiv:
        #print(type(i), i)

        if isinstance(i, str) == True:
            #print(len(i))
            summ = summ + len(i)
            print(f'Длина строки {i} добавлена к переменной summ')
        if isinstance(i, (int, float)) == True:
            #print(i)
            summ = summ + i
            print(f'Число {i} добавлено к переменной summ')
        if isinstance(i, list) == True:
            #print(i)
            summ = summ + calculate_structure_sum(i)
            print(f'Список {i} распакован')
        if isinstance(i, dict) == True:
            #print(i)
            summ = summ + calculate_structure_sum(i.items())
            print(f'Cловарь {i} распакован')
        if isinstance(i, set) == True:
            #print(i)
            summ = summ + calculate_structure_sum(sorted(i))
            print(f'Множество {i} распаковано')
        if isinstance(i, tuple) == True:
            #print(i)
            summ = summ + calculate_structure_sum(list(i))
            print(f'Кортеж {i} распакован')
    return summ


result = calculate_structure_sum(data_structure)
print()
print(f'массив значений расшифрован, сумма = {result}')