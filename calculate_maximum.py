from math import factorial

def comb(n,r):
    if n >= r:
        return factorial(n) // factorial(r) // factorial(n-r)
    else:
        return 0

def sigma(start, end, expression):
    return sum(expression(i) for i in range(start, end+1))

n = 10000
answer = sigma(0, n, lambda k: comb(n, 2*k) * comb(2*k, k))
print(answer)
print(len(str(answer)))

