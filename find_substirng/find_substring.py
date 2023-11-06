# Для заданной строки s и целого числа k вернуть длину самой длинной подстроки s, содержащей не более k различных символов.
# sliding_window

def find(s, k):
    if len(s) == 0 or k == 0:
        return 0

    if len(s) <= k:
        return len(s)

    char_frequency = {}
    max_length = 0
    unique_count = 0

    left = 0
    right = 0

    while right < len(s):
        char_frequency[s[right]] = char_frequency.get(s[right], 0) + 1

        if char_frequency[s[right]] == 1:
            unique_count += 1

        if unique_count > k:
            max_length = max(max_length, right - left)
            char_frequency[s[left]] -= 1

            if char_frequency[s[left]] == 0:
                unique_count -= 1

            left += 1

        right += 1

    max_length = max(max_length, right - left)

    return max_length

