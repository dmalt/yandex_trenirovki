"""
D. Уравнение с корнем
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Решите в целых числах уравнение:

,

a, b, c – данные целые числа: найдите все решения или сообщите, что решений в
целых числах нет.

Формат ввода
Вводятся три числа a, b и c по одному в строке.

Формат вывода
Программа должна вывести все решения уравнения в порядке возрастания, либо NO
SOLUTION (заглавными буквами), если решений нет. Если решений бесконечно много,
вывести MANY SOLUTIONS.

Пример 1
Ввод	Вывод
1
0
0
0
Пример 2
Ввод	Вывод
1
2
3
7
Пример 3
Ввод	Вывод
1
2
-3
"""


def solve(a, b, c):
    if c < 0:
        return "NO SOLUTION"
    if a == 0:
        if c ** 2 == b:
            return "MANY SOLUTIONS"
        else:
            return "NO SOLUTION"
    rhs = c ** 2 - b
    if rhs % a:
        return "NO SOLUTION"
    return rhs // a


# a, b, c = 1, 0, 0

# assert solve(1, 0, 0) == 0
# assert solve(1, 2, 3) == 7
# assert solve(1, 2, -3) == "NO SOLUTION"


a, b, c = [int(input().strip()) for _ in range(3)]
print(solve(a, b, c))
