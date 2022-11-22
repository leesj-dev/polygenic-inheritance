import collections
import itertools
import math

alleles = 5
final_result = []
linkages_result = {}
for key in range(0, len([list(item) for splits in range(1, alleles + 1) for item in itertools.combinations_with_replacement(range(1, alleles + 1), splits) if sum(item) == alleles])):
    k_values = collections.defaultdict(list)
    for element in set(tuple(sorted(item)) for item in itertools.product(*[[(list(range(0, capital_set + 1))[i], list(range(0, capital_set + 1))[j]) for i in range(0, len(list(range(0, capital_set + 1)))) for j in range(0, len(list(range(0, capital_set + 1)))) if list(range(0, capital_set + 1))[i] >= list(range(0, capital_set + 1))[j]] for capital_set in [list(item) for splits in range(1, alleles + 1) for item in itertools.combinations_with_replacement(range(1, alleles + 1), splits) if sum(item) == alleles][key]])):
        if [int(item / math.gcd(*[list([sum(item) for item in itertools.product(*[[poly[0] + poly[1], poly[0], poly[1], 0] for poly in list(element)])]).count(n) for n in range(0, sum([sum(item) for item in list(element)]) + 1)])) for item in [list([sum(item) for item in itertools.product(*[[poly[0] + poly[1], poly[0], poly[1], 0] for poly in list(element)])]).count(n) for n in range(0, sum([sum(item) for item in list(element)]) + 1)]] not in final_result:
            final_result.append([int(item / math.gcd(*[list([sum(item) for item in itertools.product(*[[poly[0] + poly[1], poly[0], poly[1], 0] for poly in list(element)])]).count(n) for n in range(0, sum([sum(item) for item in list(element)]) + 1)])) for item in [list([sum(item) for item in itertools.product(*[[poly[0] + poly[1], poly[0], poly[1], 0] for poly in list(element)])]).count(n) for n in range(0, sum([sum(item) for item in list(element)]) + 1)]])
        k_values[str([int(item / math.gcd(*[list([sum(item) for item in itertools.product(*[[poly[0] + poly[1], poly[0], poly[1], 0] for poly in list(element)])]).count(n) for n in range(0, sum([sum(item) for item in list(element)]) + 1)])) for item in [list([sum(item) for item in itertools.product(*[[poly[0] + poly[1], poly[0], poly[1], 0] for poly in list(element)])]).count(n) for n in range(0, sum([sum(item) for item in list(element)]) + 1)]])].append(list(element))
    linkages_result[str([list(item) for splits in range(1, alleles + 1) for item in itertools.combinations_with_replacement(range(1, alleles + 1), splits) if sum(item) == alleles][key])] = k_values
print(sorted(final_result, key=lambda l: (len(l), l)))
for key, value in linkages_result.items():
    print(" ".join([sorted([item.strip() for item in str(key)[1:-1].split(",")], reverse=True)[i] + "연관" for i in range(0, len(sorted([item.strip() for item in str(key)[1:-1].split(",")], reverse=True))) if sorted([item.strip() for item in str(key)[1:-1].split(",")], reverse=True)[i] != "1"] + [str([i].pop()) + "독립" for i in [*[len([i for i in range(0, len(sorted([item.strip() for item in str(key)[1:-1].split(",")], reverse=True))) if sorted([item.strip() for item in str(key)[1:-1].split(",")], reverse=True)[i] == "1"])]] if int([i].pop()) > 0]))
    for key, value in {item[0]: item[1] for item in sorted([[k, v] for k, v in dict(value).items()], key=lambda l: (len(l[0]), l))}.items():
        print(key[1:-1].replace(", ", ":"), " ", str(value)[1:-1])
