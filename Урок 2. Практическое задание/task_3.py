"""
Задание 3.	Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""


def revers_num(num, res, cnt, flag, cnt2, flag2):
    if cnt == 0 and num % 10 == 0 and num > 0:
        flag = True
    if num == 0:
        if not flag:
            print('Перевернутое число: ', res)
        elif flag:
            print('Перевернутое число: ' + '0' * cnt2 + str(res))
    else:
        cnt += 1
        last = num % 10
        if last == 0 and flag2 == True:
            cnt2 += 1
        if last != 0:
            flag2 = False
        res = res * 10 + last
        num = (num - last) // 10
        revers_num(num, res, cnt, flag, cnt2, flag2)
    cnt += 1


user_num = int(input('Введите число, которое требуется перевернуть: '))

revers_num(user_num, 0, 0, False, 0, True)
