from collections import defaultdict
from itertools import product
from itertools import combinations_with_replacement as comb
import math


def get_ratio(poly_list):
    poly_germ = [[poly[0] + poly[1], poly[0], poly[1], 0] for poly in poly_list]
    child = list([sum(x) for x in product(*poly_germ)])
    max_capital = sum([sum(x) for x in poly_list])
    ratio = [child.count(n) for n in range(0, max_capital + 1)]
    gcd_val = math.gcd(*ratio)
    ratio = [int(ratio[idx] / gcd_val for item in ratio]

    return ratio


def get_possible_capital(linkage):  # [2, 0] 꼴
    possible_capital = list(range(0, linkage + 1))
    rng = range(0, len(possible_capital))
    capital_set = [(possible_capital[i], possible_capital[j]) for i in rng for j in rng if possible_capital[i] >= possible_capital[j]] 
    
    return capital_set


alleles = 5
linkages_list = [list(x) for splits in range(1, alleles + 1) for x in comb(range(1, alleles + 1), splits) if sum(x) == alleles]
final_result = []
linkages_result = {}

for k in range(0, len(linkages_list)):
    linkages = linkages_list[k]
    k_values = defaultdict(list)
    possible_capital_list = [get_possible_capital(capital_set) for capital_set in linkages]

    for element in set(tuple(sorted(t)) for t in product(*possible_capital_list)):
        result = get_ratio(list(element))
        if result not in final_result:
            final_result.append(result)
        k_values[str(result)].append(list(element))

    linkages_result[str(linkages)] = k_values

final_result = sorted(final_result, key=lambda l: (len(l), l))  # 길이 & 숫자 크기대로 정렬
for item in final_result:
    print(item)

print("\n")

for key, value in linkages_result.items():
    link_status = sorted([x.strip() for x in str(key)[1:-1].split(",")], reverse=True)
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

    value_list = sorted([[k, v] for k, v in dict(value).items()], key=lambda l: (len(l[0]), l))  # 2차원 리스트로 변환
    value_dict = {item[0]: item[1] for item in value_list}
    for k, v in value_dict.items():
        print(k[1:-1].replace(", ", ":"), " ", str(v)[1:-1])

    print("\n")
