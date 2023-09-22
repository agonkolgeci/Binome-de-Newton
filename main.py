from math import comb

def binom(a: int, b: int, n: int):
    sum = 0
    for k in range(n + 1):
        sum += comb(n, k) * (a**k) * (b ** (n - k))

    return sum

print("Format: (a+b)**n")
a = int(input("a = "))
b = int(input("b = "))
n = int(input("n = "))

print("Result:", binom(a, b, n))