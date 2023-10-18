"""
B. Встречалось ли число раньше
Ограничение времени	3 секунды
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Во входной строке записана последовательность чисел через пробел.
Для каждого числа выведите слово YES (в отдельной строке),
если это число ранее встречалось в последовательности или NO,
если не встречалось.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.

Формат вывода
Выведите ответ на задачу.

Пример
Ввод	Вывод
1 2 3 2 3 4
        NO
        NO
        NO
        YES
        YES
        NO
"""

nums = list(map(int, input().strip().split(" ")))

s = set()
for num in nums:
    if num in s:
        print("YES")
    else:
        print("NO")
    s.add(num)