"""
E. Сумма трёх
Ограничение времени	15 секунд
Ограничение памяти	256Mb
Ввод	стандартный ввод или threesum.in
Вывод	стандартный вывод или threesum.out

Даны три массива целых чисел
A, B, C и целое число S. Найдите такие i, j, k , что Ai + Bj + Ck = S.

Формат ввода
На первой строке число
S (1 ≤ S ≤ 10^9). Следующие три строки содержат описание массивов A, B, C
в одинаковом формате: первое число задает длину n соответствующего массива
(1 ≤ n ≤ 15000), затем заданы n целых чисел от 1 до 10^9 — сам массив.

Формат вывода
Если таких i, j, k не существует, выведите единственное число '-1'.
Иначе выведите на одной строке три числа — i, j, k. Элементы массивов
нумеруются с нуля. Если ответов несколько, выведите лексикографически
минимальный.

Пример 1
Ввод	Вывод
3
2 1 2
2 3 1
2 3 1
        0 1 1
Пример 2
Ввод	Вывод
10
1 5
1 4
1 3
        -1
Пример 3
Ввод	Вывод
5
4 1 2 3 4
3 5 2 1
4 5 3 2 2
        0 1 2
"""

S = int(input().strip())
nA, *A = list(map(int, input().strip().split(" ")))
nB, *B = list(map(int, input().strip().split(" ")))
nC, *C = list(map(int, input().strip().split(" ")))


def solution(A, B, C):
    sortb = sorted(zip(B, range(len(B))))
    sortc = sorted(zip(C, range(len(C))), reverse=True)
    ans = ()
    for ia, ea in enumerate(A):
        twosum = S - ea
        i = j = 0
        while i < len(B) and j < len(C):
            x = sortb[i][0] + sortc[j][0]
            if x == twosum:
                if not ans:
                    ans = (ia, sortb[i][1], sortc[j][1])
                else:
                    ans = min(ans, (ia, sortb[i][1], sortc[j][1]))
                j += 1
            elif x > twosum:
                j += 1
            else:
                i += 1
    if not ans:
        return "-1"
    return " ".join(map(str, ans))


print(solution(A, B, C))
