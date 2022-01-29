"""
D. Угадай число
Ограничение времени	3 секунды
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n.
Беатриса пытается угадать это число, для этого она называет некоторые множества
натуральных чисел. Август отвечает Беатрисе YES, если среди названных ей чисел
есть задуманное или NO в противном случае. После нескольких заданных вопросов
Беатриса запуталась в том, какие вопросы она задавала и какие ответы получила и
просит вас помочь ей определить, какие числа мог задумать Август.

Формат ввода
Первая строка входных данных содержит число n — наибольшее число, которое мог
загадать Август. Далее идут строки, содержащие вопросы Беатрисы. Каждая строка
представляет собой набор чисел, разделенных пробелами. После каждой строки с
вопросом идет ответ Августа: YES или NO. Наконец, последняя строка входных
данных содержит одно слово HELP.

Формат вывода
Вы должны вывести (через пробел, в порядке возрастания) все числа, которые мог
задумать Август.

Пример 1
Ввод	Вывод
10
1 2 3 4 5
YES
2 4 6 8 10
NO
HELP
        1 3 5

Пример 2
Ввод	Вывод
10
1 2 3 4 5 6 7 8 9 10
YES
1
NO
2
NO
3
NO
4
NO
6
NO
7
NO
8
NO
9
NO
10
NO
HELP
        5
"""

n = int(input().strip())

is_ans = False
solution = set(range(1, n + 1))
while (string := input().strip()) != "HELP":
    if is_ans:
        if string == "YES":
            solution &= question
        elif string == "NO":
            solution -= question
        is_ans = not is_ans
    else:
        question = set(map(int, string.split(" ")))
        is_ans = not is_ans

print(" ".join(map(str, sorted(solution))))
