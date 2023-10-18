"""
C. Телефонные номера
Ограничение времени 1 секунда
Ограничение памяти  64Mb
Ввод    стандартный ввод или input.txt
Вывод   стандартный вывод или output.txt
Телефонные номера в адресной книге мобильного телефона имеют один из следующих
форматов: +7<код><номер>, 8<код><номер>, <номер>, где <номер> — это семь цифр,
а <код> — это три цифры или три цифры в круглых скобках. Если код не указан, то
считается, что он равен 495. Кроме того, в записи телефонного номера может
стоять знак “-” между любыми двумя цифрами (см. пример). На данный момент в
адресной книге телефона Васи записано всего три телефонных номера, и он хочет
записать туда еще один. Но он не может понять, не записан ли уже такой номер в
телефонной книге. Помогите ему! Два телефонных номера совпадают, если у них
равны коды и равны номера. Например, +7(916)0123456 и 89160123456 — это один и
тот же номер.

Формат ввода
В первой строке входных данных записан номер телефона, который Вася хочет
добавить в адресную книгу своего телефона. В следующих трех строках записаны
три номера телефонов, которые уже находятся в адресной книге телефона Васи.
Гарантируется, что каждая из записей соответствует одному из трех приведенных в
условии форматов.

Формат вывода
Для каждого телефонного номера в адресной книге выведите YES (заглавными
буквами), если он совпадает с тем телефонным номером, который Вася хочет
добавить в адресную книгу или NO (заглавными буквами) в противном случае.

Пример 1
Ввод    Вывод
8(495)430-23-97
+7-4-9-5-43-023-97
4-3-0-2-3-9-7
8-495-430
YES
YES
NO
Пример 2
Ввод    Вывод
86406361642
83341994118
86406361642
83341994118
NO
YES
NO
Пример 3
Ввод    Вывод
+78047952807
+78047952807
+76147514928
88047952807
YES
NO
YES
"""

target_raw_num = input().strip()
other_nums = [input().strip() for _ in range(3)]


def normalize_num(raw_num: str) -> tuple[str, str]:
    raw_num = raw_num.replace("-", "")
    if raw_num.startswith(("+7", "8")) and len(raw_num) > 7:
        if raw_num.startswith("+7"):
            raw_num = raw_num.replace("+7", "", 1)
        else:
            raw_num = raw_num.replace("8", "", 1)
        if raw_num[0] == "(":
            code = raw_num[1:4]
            norm_num = raw_num[5:]
            assert raw_num[4] == ")"
        else:
            code = raw_num[:3]
            norm_num = raw_num[3:]

    else:
        code = "495"
        norm_num = raw_num
    return code, norm_num


target_code, target_num = normalize_num(target_raw_num)

for n in other_nums:
    code, num = normalize_num(n)
    if target_code == code and target_num == num:
        print("YES")
    else:
        print("NO")
