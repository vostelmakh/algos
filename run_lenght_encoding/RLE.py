# Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28

# Если символ встречается 1 раз, он остается без изменений; 
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.

def RLE(str):
    result = ''
    same_letter_stack = []

    for letter in str:
        if len(same_letter_stack) == 0:
            same_letter_stack.append(letter)
            continue

        if same_letter_stack[-1] == letter:
            same_letter_stack.append(letter)
            continue

        result += print_short(same_letter_stack)

        same_letter_stack = []
        same_letter_stack.append(letter)

    if len(same_letter_stack) > 0:
        result += print_short(same_letter_stack)

    return result

def print_short(arr):
    if (len(arr) == 1):
        return arr[-1]
    
    return arr[-1] + str(len(arr))