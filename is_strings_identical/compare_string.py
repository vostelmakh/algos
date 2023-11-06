def no_more_than_one_change(string1: str, string2: str) -> bool:
    len1 = len(string1)
    len2 = len(string2)

    if (abs(len1 - len2) > 1):
        return False

    # Переменная для отслеживания количества различных символов
    diff_count = 0

    # Индексы для обхода символов в обеих строках
    i = 0
    j = 0

    while i < len1 and j < len2:
        if string1[i] == string2[j]:
            # переходим к следующим символам в обеих строках
            i += 1
            j += 1
            continue

        diff_count += 1

        # Если разница в длине строк равна 0, значит это замена символа
        if len1 == len2:
            i += 1
            j += 1

        # Если разница в длине строк больше 0, значит это удаление символа
        if len1 > len2:
            i += 1
        # Если разница в длине строк меньше 0, значит это вставка символа
        else:
            j += 1

        # Если количество различных символов превышает 1, то нельзя получить вторую строку с одним изменением
        if diff_count > 1:
            return False

    # Если остались еще символы в одной из строк, добавляя лишь один символ можно получить вторую строку
    if i < len1 or j < len2:
        diff_count += 1

    # Если количество различных символов равно 1 или 0, то можно получить вторую строку с одним изменением
    return diff_count == 1 or diff_count == 0


print(no_more_than_one_change('abc ', 'abc'))
print(no_more_than_one_change('abc', 'ab'))
print(no_more_than_one_change('abc', 'abc'))
