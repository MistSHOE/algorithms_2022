"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для второго скрипта
"""
from memory_profiler import profile


# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = []

# for element in my_list:
#     i = 0
#     for element_2 in my_list:
#         if element == element_2:
#             i += 1
#     if i == 1:
#         new_list.append(element)
#
# print(new_list)
#
@profile
def func_1():
    for element in my_list:
        if my_list.count(element) == 1:
            new_list.append(element)

    print(new_list)


func_1()


@profile
def func_2():
    new_list = [i for i in set(my_list) if my_list.count(i) == 1]
    print(new_list)
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     67     19.6 MiB     19.6 MiB           1   @profile
#     68                                         def func_2():
#     69     19.6 MiB      0.0 MiB          12       new_list = [i for i in set(my_list) if my_list.count(i) == 1]
#     70     19.6 MiB      0.0 MiB           1       print(new_list)

func_2()

