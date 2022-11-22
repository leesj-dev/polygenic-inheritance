import itertools

"""
gene_ini = {
    "가": ["A", "a"],  # A = a
    "나": ["B", "b"],  # B > b
    "다": ["E", "F", "G"],  # E = F > G
    "라": ["T", "T*"],  # T ? T*
}

연관 유전: {"A1": [["A", "b"], ["A, B"]],
          "A2": [["E"], ["F"]],
          "X": [["T"], ["T*"]],
}

dominants = {'A = a', 'B > b', 'E = F > G', 'T ? T*'}
"""

linkage = {"A1": ["가", "나"], "A2": ["다"], "X": ["라"]}  # Autosomal 1st chromosome 연관
# 반성 유전의 경우, 어떻게 처리할 지가 상당히 난관임 (성별까지 모두 고려해야 함)

gene_dict_full = {
    "가": [[{"A", "a"}]],  # A = a
    "나": [[{"B"}, {"b"}]],  # B > b
    "다": [[{"E", "F"}, {"G"}]],  # E = F > G
    "라": [[{"T"}, {"T*"}], [{"T*"}, {"T"}], [{"T", "T*"}]],  # T > T*
}


class Person:
    def __init__(self, sex, parents):
        self.sex = sex
        self.father = parents[0]
        self.mother = parents[1]
        self.children = []
        self.geno = dict.fromkeys(gene_list, None)
        self.pheno = dict.fromkeys(gene_list, None)

    def add_genotype(self, key, genotype):
        self.geno[key] = sorted([*genotype])
        self.pheno[key] = find_pheno_by_geno(genotype)

    def add_phenotype(self, key, phenotype):
        self.pheno[key] = {*phenotype}

    def get_children_info(self):
        for person in family:
            if self in (person.father, person.mother):
                self.children.append(person)


dominant_list = gene_dict_full.values()
dominant_possible = list(itertools.product(*dominant_list))

for case in dominant_possible:
    gene_dict = dict(zip(gene_dict_full.keys(), case))
    gene_list = gene_dict.keys()
    print(gene_dict)

    def find_pheno_by_geno(genotype) -> set:
        genotype_set = {*genotype}

        target_key = {
            key
            for key, value in gene_dict.items()
            for _set in value
            for item in _set
            if item in genotype
        }.pop()
        target_dominants = gene_dict[target_key]

        i = 0
        while True:
            intersection = target_dominants[i] & genotype_set
            if len(intersection) == 0:
                i = i + 1
            else:
                return intersection

    dad = Person("M", [None, None])
    mom = Person("F", [None, None])
    daughter = Person("F", [dad, mom])
    son = Person("M", [dad, mom])
    family = [dad, mom, daughter, son]

    dad.get_children_info()
    mom.get_children_info()

    dad.add_genotype("가", "Aa")
    dad.add_genotype("나", "BB")
    dad.add_genotype("다", "FG")
    print(dad.sex, dad.father, dad.mother, dad.children, dad.geno, dad.pheno)
