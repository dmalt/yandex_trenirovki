"""
B. Номер левого и правого вхождения
Ограничение времени	2 секунды
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Требуется определить в заданном массиве номер самого левого и самого правого
элемента, равного искомому числу.

Формат ввода
В первой строке вводится одно натуральное число N, не превосходящее 10^5:
количество чисел в массиве. Во второй строке вводятся N натуральных чисел,
не превосходящих 10^9, каждое следующее не меньше предыдущего. В третьей
строке вводится количество искомых чисел M – натуральное число, не
превосходящее 10^6. В четвертой строке вводится M натуральных чисел, не
превосходящих 10^9.

Формат вывода
Для каждого запроса выведите в отдельной строке через пробел два числа: номер
элемента самого левого и самого правого элементов массива, равных
числу-запросу. Элементы массива нумеруются с единицы. Если в массиве нет такого
числа, выведите в соответствующей строке два нуля, разделенных пробелом.

Пример 1
Ввод	Вывод
4
1 2 2 3
4
4 3 2 1
        0 0
        4 4
        2 3
        1 1
Пример 2
Ввод	Вывод
10
1 2 3 4 5 6 7 7 8 9
10
7 3 3 1 3 7 9 7 7 10
        7 8
        3 3
        3 3
        1 1
        3 3
        7 8
        10 10
        7 8
        7 8
        0 0
Пример 3
Ввод	Вывод
10
1 3 3 3 3 6 8 8 9 10
10
2 9 6 4 2 9 3 7 9 7
        0 0
        9 9
        6 6
        0 0
        0 0
        9 9
        2 5
        0 0
        9 9
        0 0
"""

N = int(input().strip())
nums = list(map(int, input().strip().split(" ")))
M = int(input().strip())
queries = list(map(int, input().strip().split(" ")))


def lbinsearch(lo, hi, check, checkparams):
    while lo < hi:
        m = (lo + hi) // 2
        if check(m, checkparams):
            hi = m
        else:
            lo = m + 1
    return lo


def checkge(index, params):
    val, seq = params
    return seq[index] >= val


def checkgt(index, params):
    val, seq = params
    return seq[index] > val


def findfirst(seq, val, check):
    ind = lbinsearch(0, len(seq) - 1, check, (val, seq))
    if not check(ind, (val, seq)):
        ind = len(seq)
    return ind


def findrepeated(seq, val):
    indexge = findfirst(seq, val, checkge)
    indexgt = findfirst(seq, val, checkgt)
    if indexge == len(seq) or indexge == indexgt:
        return (0, 0)
    return (indexge + 1, indexgt)


for q in queries:
    ans = findrepeated(nums, q)
    print(" ".join(map(str, ans)))
