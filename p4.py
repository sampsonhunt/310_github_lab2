def is_palindrome(n):
    return str(n) == str(n)[::-1]

max_pal = 0
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        product = j * i
        if is_palindrome(product) and product > max_pal:
            print i, j
            max_pal = product
print max_pal
