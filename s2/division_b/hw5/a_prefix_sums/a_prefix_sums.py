"""
A. Префиксные суммы
Ограничение времени	1 секунда
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

В этой задаче вам нужно будет много раз отвечать на запрос «Найдите сумму чисел
на отрезке в массиве».

Формат ввода
В первой строке записано два целых числа n и q (1 ≤ n , q ≤ 3 * 10 ^ 5) -
размер массива и количество запросов. Во второй строке записаны
n целых чисел a i (1 ≤ ai ≤ 10^9) - сам массив. Далее в q
строках описаны запросы к массиву. Каждый запрос описывается двумя числами
l, r (1 ≤ l ≤ r ≤ n) - левой и правой границей отрезка,
на котором нужно найти сумму.

Формат вывода
Для каждого запроса в отдельной строке выведите единственное число - сумму на
соответствующем отрезке.

Пример
Ввод	Вывод
4 10
1 2 3 4
1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4
        1
        3
        6
        10
        2
        5
        9
        3
        7
        4
"""

n, q = list(map(int, input().strip().split(" ")))
array = list(map(int, input().strip().split(" ")))
queries = [list(map(int, input().strip().split(" "))) for _ in range(q)]


prefixsums = [0] * (n + 1)
for i in range(1, n + 1):
    prefixsums[i] = prefixsums[i - 1] + array[i - 1]

for query in queries:
    print(prefixsums[query[1]] - prefixsums[query[0] - 1])