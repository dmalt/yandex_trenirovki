"""
E. Покрытие K отрезками
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Даны n точек на прямой, нужно покрыть их k отрезками одинаковой длины l.
Найдите минимальное l.

Формат ввода
На первой строке n (1 ≤ n ≤ 10^5) и k (1 ≤ k ≤ n).
На второй n чисел xi (∣xi∣ ≤ 10^9).

Формат вывода
Минимальное такое l, что точки можно покрыть k отрезками длины l.

Пример
Ввод	Вывод
6 2
1 2 3 9 8 7
        2
"""


n, k = list(map(int, input().strip().split(" ")))
coords = sorted(map(int, input().strip().split(" ")))


def lbinsearch(lo, hi, check, checkparams):
    while lo < hi:
        m = (lo + hi) // 2
        if check(m, checkparams):
            hi = m
        else:
            lo = m + 1
    return lo


def checkcoveringnumgtk(l, params):
    k, coords = params

    if (coords[-1] - coords[0]) <= k * l:
        return True

    cprev = coords[0]
    covercnt = 1
    for c in coords:
        if l + cprev < c:
            cprev = c
            covercnt += 1
    return covercnt <= k


ans = lbinsearch(0, coords[-1] - coords[0], checkcoveringnumgtk, (k, coords))
print(ans)
