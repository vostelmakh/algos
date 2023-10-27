def longest_increasing_subsequence(arr):
    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Задача. Дан массив из N целых чисел arr. 
# Найдите длину максимальной возрастающей подпоследовательности в этом массиве. 
# Например, при arr=[2, 3, 6, 4, 1, 3, 5, 4, 7] искомая подпоследовательность - [2, 3, 4, 5, 7] и поэтому ответ равен 5.