"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""

# Задание № 2


def number(x, negative, positive):
    print(x)

    if x == 0:
        print(f'Количество нечетныых цифр - {negative}, Количество четных цифр - {positive}')

    else:
        result = x % 10
        if result % 2 == 0:
            positive += 1
        else:
            negative += 1

        return number((x // 10), negative, positive)


number(321, 0, 0)