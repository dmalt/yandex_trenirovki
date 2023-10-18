"""
D. Наполненность котятами
Ограничение времени	2 секунды
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

На прямой в точках a1 , a2 , ... , an (возможно, совпадающих) сидят n котят.
На той же прямой лежат m отрезков [ l1 , r1 ] , [ l2, r2 ] , ... , [ lm, rm ].
Нужно для каждого отрезка узнать
его наполненность котятами — сколько котят сидит на отрезке.

Формат ввода
На первой строке n и m (1 ≤ n , m ≤ 10^5).
На второй строке n целых чисел ai (0 ≤ ai ≤ 10^9).
Следующие m строк содержат пары целых чисел li, ri (0 ≤ li ≤ ri ≤ 10^9).

Формат вывода
Выведите m целых чисел. i-е число — наполненность котятами i-го отрезка.
"""

START = -1
END = 1
KITTEN = 0

n, m = list(map(int, input().split()))

kittens = list(map(int, input().split()))
intervals = [list(map(int, input().split())) for _ in range(m)]


def countkittens(intervals, kittens):
    events = []
    for i, (l, r) in enumerate(intervals):
        events.append((l, START, i))
        events.append((r, END, i))
    for i, k in enumerate(kittens):
        events.append((k, KITTEN, i))
    events.sort()

    kittenscntend = [0] * len(intervals)
    kittenscntstart = [0] * len(intervals)
    kittenscnt = 0

    for ev in events:
        if ev[1] == START:
            kittenscntstart[ev[2]] = kittenscnt
        elif ev[1] == END:
            kittenscntend[ev[2]] = kittenscnt
        elif ev[1] == KITTEN:
            kittenscnt += 1
    return [e - s for e, s in zip(kittenscntend, kittenscntstart)]


for cnt in countkittens(intervals, kittens):
    print(cnt)
