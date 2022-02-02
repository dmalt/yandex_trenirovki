"""
C. Минимальное покрытие
Ограничение времени	3 секунды
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

На прямой задано некоторое множество отрезков с целочисленными координатами
концов [Li, Ri]. Выберите среди данного множества подмножество отрезков,
целиком покрывающее отрезок [0, M], (M — натуральное число), содержащее
наименьшее число отрезков.

Формат ввода
В первой строке указана константа M (1 ≤ M ≤ 5000). В каждой последующей строке
записана пара чисел Li и Ri (Li, Ri ≤ 50000), задающая координаты левого и
правого концов отрезков. Список завершается парой нулей. Общее число отрезков
не превышает 100 000.

Формат вывода
В первой строке выходного файла выведите минимальное число отрезков,
необходимое для покрытия отрезка [0; M]. Далее выведите список покрывающего
подмножества, упорядоченный по возрастанию координат левых концов отрезков.
Список отрезков выводится в том же формате, что и во входe. Завершающие два
нуля выводить не нужно. Если покрытие отрезка [0, M] исходным множеством
отрезков [Li, Ri] невозможно, то следует вывести единственную фразу “No
solution”.

Пример 1
Ввод	Вывод
1
-1 0
-5 -3
2 5
0 0
        No solution
Пример 2
Ввод	Вывод
1
-1 0
0 1
0 0
        1
        0 1
"""


def findfirstinterval(coords, leftbound):
    indmaxright = None
    maxright = leftbound
    for i, (lo, hi) in enumerate(coords):
        if hi <= leftbound:
            continue
        elif lo <= leftbound:
            if hi > maxright:
                maxright = hi
                indmaxright = i
        else:
            break

    return indmaxright


def findcoverage(coords, leftbound, rightbound):
    if not coords:
        return None
    coords.sort(key=lambda x: (x[0], -x[1]))
    indmaxright = findfirstinterval(coords, leftbound)
    if indmaxright is None:
        return None

    ans = [coords[indmaxright]]
    maxcoords = ans[-1]

    for lo, hi in coords[indmaxright + 1 :]:
        if hi <= ans[-1][1]:
            continue
        if lo <= ans[-1][1]:
            maxcoords = max([lo, hi], maxcoords, key=lambda x: x[1])
        elif lo > ans[-1][1] and maxcoords != ans[-1]:
            ans.append(maxcoords)
            if ans[-1][1] >= rightbound:
                return ans
            if hi <= ans[-1][1]:
                continue
            if lo <= ans[-1][1]:
                maxcoords = max([lo, hi], maxcoords, key=lambda x: x[1])
            else:
                return None
            # process this new lo and hi
        else:
            return None
    if maxcoords != ans[-1]:
        ans.append(maxcoords)
    if rightbound > ans[-1][1]:
        return None
    return ans


def main():
    with open("input.txt", "r") as f:
        M = int(f.readline().strip())
        coords = []
        while (input := list(map(int, f.readline().strip().split()))) != [
            0,
            0,
        ]:
            coords.append(input)
    ans = findcoverage(coords, 0, M)
    if ans is None:
        print("No solution")
    else:
        print(len(ans))
        for c in ans:
            print(" ".join(map(str, c)))


def test():
    coords = [[-1, 0], [-5, -3], [2, 5]]
    M = 1
    assert findcoverage(coords, 0, M) is None
    M = 1
    coords = [[-1, 0], [0, 1], [0, 0]]
    assert findcoverage(coords, 0, M) == [[0, 1]]
    M = 10
    coords = [[-2, -1], [-1, 2], [0, 1], [2, 3], [3, 10]]
    assert findcoverage(coords, 0, M) == [[-1, 2], [2, 3], [3, 10]]


# test()
main()
