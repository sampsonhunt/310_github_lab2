"""
WORK IN PROGRESS
P:495

Let W(n,k) be the number of ways in which n can be written as the product of k distinct positive integers.

For example, W(144,4) = 7. There are 7 ways in which 144 can be written as a product of 4 distinct positive integers:

    144 = 1×2×4×18
    144 = 1×2×8×9
    144 = 1×2×3×24
    144 = 1×2×6×12
    144 = 1×3×4×12
    144 = 1×3×6×8
    144 = 2×3×4×6

Note that permutations of the integers themselves are not considered distinct.

Furthermore, W(100!,10) modulo 1 000 000 007 = 287549200.

Find W(10000!,30) modulo 1 000 000 007.

"""
def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
# Find all permutations of n x k
# Ex: 144 = 1x2x4x18
def mystery_function(n, k):
    total = 1
    count = 0
    existing_factors = factors(n)
    print existing_factors

    for factor in existing_factors:
        total *= factor
        count += 1
        if total == n:
            return count




print mystery_function(144,4)
