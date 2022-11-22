from itertools import product
from itertools import combinations_with_replacement as comb
from fractions import Fraction
import math

alleles = 10
odd_total = set(range(1, 1000, 2))
odd_exists = set()


def get_ratio(poly_list):
    poly_germ = [[poly[0] + poly[1], poly[0], poly[1], 0] for poly in poly_list]
    child = list([sum(x) for x in product(*poly_germ)])
    max_capital = sum([sum(x) for x in poly_list])
    ratio = [child.count(n) for n in range(0, max_capital + 1)]
    ratio_gcd = [int(item / math.gcd(*ratio)) for item in ratio]

    for item in ratio_gcd:
        odd_exists.add(Fraction(item, sum(ratio_gcd)).numerator)


def get_possible_capital(linkage):
    possible_capital = list(range(0, linkage + 1))
    rng = range(0, len(possible_capital))
    capital_set = [(possible_capital[i], possible_capital[j]) for i in rng for j in rng if possible_capital[i] >= possible_capital[j]]

    return capital_set


linkages_list = [list(x) for splits in range(1, alleles + 1) for x in comb(range(1, alleles + 1), splits) if sum(x) == alleles]

for k in range(0, len(linkages_list)):
    linkages = linkages_list[k]
    possible_capital_list = [get_possible_capital(capital_set) for capital_set in linkages]

    for element in set(tuple(sorted(t)) for t in product(*possible_capital_list)):
        get_ratio(list(element))

print(odd_total - odd_exists)
