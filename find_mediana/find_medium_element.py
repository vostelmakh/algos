# def find_medium_element(a, b, c):
#     if a > b and a < c:
#         return a
    
#     if b > a and b < c:
#         return b
    
#     if c > a and c < b:
#         return c
    
#     return None

def find_medium_element(a, b, c):
    x = max(a, b)
    y = max(a, c)

    if (x == y):
        return max(b, c)
    else:
        return min(x, y)