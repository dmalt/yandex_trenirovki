"""
C. Корень кубического уравнения
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	cubroot.in
Вывод	cubroot.out

Дано кубическое уравнение ax3+bx2+cx+d=0 (a≠0). Известно, что у этого уравнения
есть ровно один корень. Требуется его найти.

Формат ввода
Во входном файле через пробел записаны четыре целых числа:
-1000 <= a, b, c, d <= 1000.

Формат вывода
Выведите единственный корень уравнения с точностью не менее 5 знаков после
десятичной точки.

Пример 1
Ввод	Вывод
1 -3 3 -1
        1.0000036491
Пример 2
Ввод	Вывод
-1 -6 -12 -7
        -1.0000000111
"""


with open("cubroot.in", "r") as f:
    a, b, c, d = list(map(int, f.readline().strip().split(" ")))


def fbinsearch(lo, hi, eps, check, checkparams):
    while lo + eps < hi:
        m = (lo + hi) / 2
        if check(m, checkparams):
            hi = m
        else:
            lo = m
    return lo


def checkpositive(val, params):
    a, b, c, d = params
    return a * val ** 3 + b * val ** 2 + c * val + d > 0


def findroot(a, b, c, d, eps):
    if a > 0:
        return fbinsearch(-2000, 2000, eps, checkpositive, (a, b, c, d))
    else:
        return fbinsearch(-2000, 2000, eps, checkpositive, (-a, -b, -c, -d))


with open("cubroot.out", "w") as f:
    f.write(str(findroot(a, b, c, d, 1e-6)))
