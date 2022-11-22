from math import factorial

def comb(n,r):
    return factorial(n) // factorial(r) // factorial(n-r)

def sigma(start, end, expression):
    return sum(expression(i) for i in range(start, end+1))

def phenotype_calc(n):
    phenotype = []
    if n % 2 == 0:
        l = n // 2  # n = 2*l
        for k in range(0, l+1):
            if k != l:
                phenotype.append(sigma(0, k, lambda i: comb(2*l, i) * comb(2*l-i, 2*k-2*i)))
                phenotype.append(sigma(0, k, lambda i: comb(2*l, i) * comb(2*l-i, 2*k+1-2*i)))
            elif k == l:
                phenotype = phenotype + [sigma(0, k, lambda i: comb(2*l, i) * comb(2*l-i, 2*k-2*i))] + phenotype[::-1]

    elif n % 2 == 1:
        l = (n+1) // 2  # n = 2*l-1
        for k in range(0, l):
            if k != l - 1:
                phenotype.append(sigma(0, k, lambda i: comb(2*l-1, i) * comb(2*l-1-i, 2*k-2*i)))
                phenotype.append(sigma(0, k, lambda i: comb(2*l-1, i) * comb(2*l-1-i, 2*k+1-2*i)))
            elif k == l - 1:
                phenotype.append(sigma(0, k, lambda i: comb(2*l-1, i) * comb(2*l-1-i, 2*k-2*i)))
                phenotype = phenotype + [sigma(0, k, lambda i: comb(2*l-1, i) * comb(2*l-1-i, 2*k+1-2*i))] + phenotype[::-1]

    return phenotype

for j in range(0, 11):
    print(j, ":", phenotype_calc(j))


'''

sum_even = 2*sigma(0, l-1, lambda k: sigma(0, k, lambda i: comb(2*l, i) * comb(2*l-i+1, 2*k-2*i+1))) + sigma(0, l, lambda i: comb(2*l, i) * comb(2*l-i, 2*l-2*i))

sum_odd = 2*sigma(0, l-1, lambda k: sigma(0, k, lambda i: comb(2*l-1, i) * comb(2*l-i, 2*k-2*i+1))) - sigma(0, l-1, lambda i: comb(2*l-1, i) * comb(2*l-1-i, 2*l-1-2*i))

print(sum_even, 3**(2*l), sum_odd, 3**(2*l-1))

'''