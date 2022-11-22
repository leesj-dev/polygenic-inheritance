from collections import defaultdict
from itertools import product
from itertools import combinations_with_replacement as comb
from fractions import Fraction
import math

alleles = 10

def get_ratio(poly_list):
    poly_germ = [[poly[0] + poly[1], poly[0], poly[1], 0] for poly in poly_list]
    child = list([sum(x) for x in product(*poly_germ)])
    max_capital = sum([sum(x) for x in poly_list])
    ratio = [child.count(n) for n in range(0, max_capital + 1)]
    ratio_gcd = [int(item / math.gcd(*ratio)) for item in ratio]
    ratio_new = []

    for item in ratio_gcd:
        ratio_new.append(Fraction(item, sum(ratio_gcd)))

    return ratio_new


def get_possible_capital(linkage):
    possible_capital = list(range(0, linkage + 1))
    rng = range(0, len(possible_capital))
    capital_set = [(possible_capital[i], possible_capital[j]) for i in rng for j in rng if possible_capital[i] >= possible_capital[j]]

    return capital_set


linkages_list = [list(x) for splits in range(1, alleles + 1) for x in comb(range(1, alleles + 1), splits) if sum(x) == alleles]
linkages_result = {}

for k in range(0, len(linkages_list)):
    linkages = linkages_list[k]
    k_values = defaultdict(list)
    possible_capital_list = [get_possible_capital(capital_set) for capital_set in linkages]

    for element in set(tuple(sorted(t)) for t in product(*possible_capital_list)):
        result = get_ratio(list(element))
        k_values[str(result)].append(list(element))

    linkages_result[str(linkages)] = k_values


def link_status_parser(link):
    link_new = []
    independent_cnt = 0

    for i in range(0, len(link)):
        if link[i] == "1":
            independent_cnt = independent_cnt + 1

        else:
            link_new.append(link[i] + "연관")

        if independent_cnt > 0:
            link_new.append(str(independent_cnt) + "독립")

        return " ".join(link_new)


for key, value in linkages_result.items():
    link_status = sorted([x.strip() for x in str(key)[1:-1].split(",")], reverse=True)
    link_status_str = link_status_parser(link_status)
    value_list = sorted([[k, v] for k, v in dict(value).items()], key=lambda l: (len(l[0]), l))
    value_dict = {item[0]: item[1] for item in value_list}

    for k, v in value_dict.items():
        print(link_status_str, k[1:-1].replace(", ", " : ").replace("'", ""), " ", str(v)[1:-1])

    print("\n")

