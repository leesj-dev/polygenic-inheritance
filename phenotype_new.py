import time
start = time.time()

n = 0
i = 1
primes = []
while i < 100:
    i += 1
    cnt = 1
    for j in range(2, i):
        if i % j == 0:
            cnt = 0
            break
    if cnt == 1:
        primes.append(i)
        n += 1


def is_prime(list_chk):
    flg = True
    for item in list_chk:
        if item not in primes:
            return False

    if flg is True:
        return True

row = [1]
row_prime = []
N = 1000

for alleles in range(1, N + 1):
    row = [sum(t) for t in zip([0, 0] + row, [0] + row + [0], row + [0, 0])]

    for num in range(0, len(row)):
        item = row[num]
        split_two = []
        item_str = str(item)
        i = 0

        if len(item_str) % 2 == 0:
            while i <= len(item_str) - 2:
                split_two.append(int(str(item)[i : i + 2]))
                i += 2
        else:
            while i <= len(item_str) - 3:
                split_two.append(int(str(item)[i : i + 2]))
                i += 2
            split_two.append(int(str(item)[len(item_str) - 1]))

        if is_prime(split_two) is True and split_two not in row_prime:
            row_prime.append([alleles, num, split_two])

# print(row_prime)
prime_sum = []

for k in range(0, len(row_prime)):
    prime_sum.append(sum(row_prime[k][2]))

idx = prime_sum.index(max(prime_sum))
print(row_prime[idx], sum(row_prime[idx][2]))

end = time.time()
print(1000*(end - start), 'ms')