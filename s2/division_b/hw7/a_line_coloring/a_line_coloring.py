"""
A. Закраска прямой
Ограничение времени	3 секунды
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

На числовой прямой окрасили N отрезков. Известны координаты левого и правого
концов каждого отрезка (Li и Ri). Найти длину окрашенной части числовой прямой.

Формат ввода
В первой строке находится число N, в следующих N строках - пары Li и Ri. Li и
Ri - целые, -10^9 ≤ Li ≤ Ri ≤ 10^9, 1 ≤ N ≤ 15 000

Формат вывода
Вывести одно число - длину окрашенной части прямой.

Пример 1
Ввод	Вывод
1
10 20
        10
Пример 2
Ввод	Вывод
1
10 10
        0
Пример 3
Ввод	Вывод
2
10 20
20 40
        30
"""

N = int(input().strip())
coords = [list(map(int, input().strip().split(" "))) for _ in range(N)]

START = 1
END = -1


def linecoloring(coords):
    events = []
    for c in coords:
        events.append((c[0], START))
        events.append((c[1], END))
    events.sort()
    totallength = 0
    intersectcnt = 0
    for iev, ev in enumerate(events):
        if intersectcnt > 0:
            totallength += ev[0] - events[iev - 1][0]
        if ev[1] == START:
            intersectcnt += 1
        else:
            intersectcnt -= 1
    return totallength


print(linecoloring(coords))
