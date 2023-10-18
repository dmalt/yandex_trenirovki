"""
E. Полярные прямоугольники
Ограничение времени	5 секунд
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Вася недавно изучил полярную систему координат. А именно, он изучил понятие
полярного прямоугольника. Пусть задана стандартная декартова плоскость. Если на
ней нарисовать две окружности с центром в начале координат, то область,
находящаяся между ними, называется кольцом (на рисунке обозначена синим). Если
на ней нарисовать два луча, то область, заметаемая первым лучом при движении ко
второму, называется углом
(т.е. область между этими двумя лучами, на рисунке обозначена зеленым).
Полярным прямоугольником называется пересечение некоторого угла с некоторым
кольцом (на рисунке обозначено красным).

Задано несколько полярных прямоугольников. Найдите площадь их пересечения.
Помните, что пересечение полярных прямоугольников может состоять из нескольких
частей!

Формат ввода
В первой строке вводится целое число N — количество прямоугольников
(1 ≤ N ≤ 100 000). Далее в N строках содержится описание прямоугольников.
Каждый прямоугольник описывается четверкой действительных чисел r1, r2, φ1, φ2,
где r1, r2 обозначают радиусы окружностей, образующих кольцо (r1 < r2), а φ1,
φ2 обозначают углы, образованные первым и вторым лучами с осью абсцисс,
заданные в радианах. При этом заметается область от первого луча до второго в
направлении против часовой стрелки (т.е. возрастания углов), даже в случае,
когда φ1 > φ2. Все числа заданы максимум с шестью знаками после десятичной
точки. Углы лежат в полуинтервале 0, 2π, а радиусы не превосходят 10^6.
Гарантируется, что φ1 ≠ φ2.

Формат вывода
Выведите единственное число — площадь искомого пересечения.
Ответ будет считаться правильным, если его абсолютная или относительная
погрешность не будет превышать 10^-6.

Пример 1
Ввод	Вывод
2
1 3 0 3
2 4 1.5 4.5
        3.7500000000
Пример 2
Ввод	Вывод
2
1 2 0 3
1 2 2 1
        3.0000000000

"""

import math


def intersectradii(rects):
    inner = float("-inf")
    outer = float("inf")
    for nowinner, nowouter, _, _ in rects:
        if nowinner > outer or nowouter < inner:
            return (0, 0)
        if inner <= nowinner <= outer:
            inner = nowinner
        if inner <= nowouter <= outer:
            outer = nowouter
    return inner, outer


def intersectangle(rects):
    START = 1
    END = -1
    events = []
    for i, rect in enumerate(rects):
        events.append((rect[2], START, i))
        events.append((rect[3], END, i))
    events.sort()

    intersectcnt = 0
    laststartangle = None
    opened = set()
    for ev in events:
        if ev[1] == START:
            intersectcnt += 1
            opened.add(ev[2])
            if intersectcnt == len(rects):
                laststartangle = ev[0]
        if ev[1] == END and ev[2] in opened:
            intersectcnt -= 1
            laststartangle = None
    totalangle = 0
    for ev in events:
        if ev[1] == START:
            intersectcnt += 1
            if intersectcnt == len(rects):
                laststartangle = ev[0]
        if ev[1] == END:
            intersectcnt -= 1
            if laststartangle is not None:
                totalangle += (ev[0] - laststartangle) % (math.pi * 2)
            laststartangle = None
    return totalangle


def intersectionarea(rects):
    r1, r2 = intersectradii(rects)
    if r1 == 0 and r2 == 0:
        return 0
    angle = intersectangle(rects)
    return (r2 ** 2 - r1 ** 2) * angle / 2


def test():
    rects = [
        (0, 2, 0, math.pi / 2),
        (1, 3, 0, math.pi / 2),
        (1, 1.5, math.pi / 3, math.pi / 4),
    ]
    assert intersectradii(rects) == (1, 1.5)
    print(intersectangle(rects))


def main():
    N = int(input().strip())
    rects = [list(map(float, input().split())) for _ in range(N)]
    print(intersectionarea(rects))


# test()
main()
