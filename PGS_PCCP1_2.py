import itertools


def solution(ability):
    answer = 0
    e = len(ability[0])
    s = len(ability)

    for comb in list(itertools.permutations(range(s), e)):
        answer = max(answer, sum([ability[c][i] for i, c in enumerate(comb)]))
    return answer


print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))