"""
B. Максимальная сумма
Ограничение времени	3 секунды
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

В этой задаче вам требуется найти непустой отрезок массива с максимальной
суммой.

Формат ввода
В первой строке входных данных записано единственное число
n (1 ≤ n ≤ 3 * 10^5) - размер массива. Во второй строке записано n
целых чисел ai ( − 10^9 ≤ ai ≤ 10^9) - сам массив.

Формат вывода
Выведите одно число - максимальную сумму на отрезке в данном массиве.

Пример 1
Ввод	Вывод
4
1 2 3 4
        10
Пример 2
Ввод	Вывод
4
5 4 -10 4
        9
"""


n = int(input().strip())
array = map(int, input().strip().split(" "))

minprefix = nowprefix = 0
maxsum = float("-inf")

for a in array:
    nowprefix += a
    maxsum = max(maxsum, nowprefix - minprefix)
    minprefix = min(nowprefix, minprefix)

print(maxsum)