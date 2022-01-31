"""
A. Быстрый поиск в массиве
Ограничение времени	3 секунды
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Дан массив из N целых чисел. Все числа от -10^9 до 10^9 .
Нужно уметь отвечать на запросы вида “Cколько чисел имеют значения от L до R?”.

Формат ввода
Число N (1 ≤ N ≤ 10^5).
Далее N целых чисел. Затем число запросов K (1 ≤ K ≤ 10^5).
Далее K пар чисел L, R (-10^9 ≤ L ≤ R ≤ 10^9) — собственно запросы.

Формат вывода
Выведите K чисел — ответы на запросы.

Пример
Ввод	Вывод
5
10 1 10 3 4
4
1 10
2 9
3 4
2 2
        5 2 2 0
"""

N = int(input().strip())
numbers = sorted(map(int, input().strip().split(" ")))
K = int(input().strip())
queries = [list(map(int, input().strip().split(" "))) for _ in range(K)]


def lbinsearch(lo, hi, check, checkattrs):
    while lo < hi:
        m = (hi + lo) // 2
        if check(m, checkattrs):
            hi = m
        else:
            lo = m + 1
    return lo


def rbinsearch(lo, hi, check, checkattrs):
    while lo < hi:
        m = (hi + lo + 1) // 2
        if check(m, checkattrs):
            lo = m
        else:
            hi = m - 1
    return lo


def checkge(m, params):
    L, arr = params
    return arr[m] >= L


def checkle(m, params):
    R, arr = params
    return arr[m] <= R


def findfirst(array, L):
    index = lbinsearch(0, N - 1, checkge, (L, array))
    if array[index] < L:
        index = N
    return index


def findlast(array, R):
    index = rbinsearch(0, N - 1, checkle, (R, array))
    if array[index] > R:
        index = -1
    return index


def solution(array, queries):
    for query in queries:
        lo = findfirst(array, query[0])
        hi = findlast(array, query[1])
        if lo <= hi:
            print(hi - lo + 1, end=" ")
        else:
            print(0, end=" ")
    print()


solution(numbers, queries)
