from collections import defaultdict
from itertools import product
from itertools import combinations_with_replacement as comb
import math


def get_ratio(poly_list):
    poly_germ = []
    for poly in poly_list:
        poly_germ.append([poly[0] + poly[1], poly[0], poly[1], 0])

    child = list([sum(x) for x in product(*poly_germ)])
    max_capital = sum([sum(x) for x in poly_list])
    ratio = []
    for n in range(0, max_capital + 1):
        ratio.append(child.count(n))

    gcd_val = math.gcd(*ratio)
    for idx in range(0, len(ratio)):
        ratio[idx] = int(ratio[idx] / gcd_val)

    return (ratio, poly_list)


def get_possible_capital(linkage):  # [2, 0] 꼴
    possible_capital = list(range(0, linkage + 1))
    capital_set = []
    for i in range(0, len(possible_capital)):
        for j in range(0, len(possible_capital)):
            if possible_capital[i] >= possible_capital[j]:
                capital_set.append(tuple([possible_capital[i], possible_capital[j]]))

    return capital_set


alleles = 5
linkages_list = []  # [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]] 꼴

for splits in range(1, alleles + 1):
    for x in comb(range(1, alleles + 1), splits):
        if sum(x) == alleles:
            linkages_list.append(list(x))

final_result = []
k_values = {}
linkages_result = {}

for k in range(0, len(linkages_list)):
    linkages = linkages_list[k]
    possible_capital_list = []
    k_values = defaultdict(list)

    for capital_set in linkages:
        possible_capital_list.append(get_possible_capital(capital_set))

    for element in set(tuple(sorted(t)) for t in product(*possible_capital_list)):
        result = get_ratio(list(element))

        if result[0] not in final_result:
            final_result.append(result[0])

        k_values[str(result[0])].append(result[1])

    linkages_result[str(linkages)] = k_values

final_result = sorted(final_result, key=lambda l: (len(l), l))  # 길이 & 숫자 크기대로 정렬
for item in final_result:
    print(item)

print("\n")


for key1, value1 in linkages_result.items():
    link_status = sorted([x.strip() for x in str(key1)[1:-1].split(",")], reverse=True)
    link_status_new = []
    independent_cnt = 0

    for i in range(0, len(link_status)):
        if link_status[i] == "1":
            independent_cnt = independent_cnt + 1

        else:
            link_status_new.append(link_status[i] + "연관")

    if independent_cnt > 0:
        link_status_new.append(str(independent_cnt) + "독립")

    print(" ".join(link_status_new))

    value1_list = []
    for k, v in dict(value1).items():  # 2차원 리스트로 변환
        value1_list.append([k, v])

    value1_list = sorted(value1_list, key=lambda l: (len(l[0]), l))
    value1_dict = {item[0]: item[1] for item in value1_list}
    for k, v in value1_dict.items():
        print(k[1:-1].replace(", ", ":"), " ", str(v)[1:-1])

    print("\n")
