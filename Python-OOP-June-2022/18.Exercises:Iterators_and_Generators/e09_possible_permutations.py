from itertools import permutations


def possible_permutations(elements):
    list_perm = permutations(elements)
    for perm in list_perm:
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]
