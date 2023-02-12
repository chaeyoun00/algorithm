max_sum = 0

def dfs(ability, idx, cur_sum, v):
    global max_sum
    
    if idx == len(ability[0]):
        max_sum = max(max_sum, cur_sum)
        return
    
    for i in range(len(ability)):
        if v[i] == 1:
            continue
        v[i] = 1
        cur_sum += ability[i][idx]
        dfs(ability, idx + 1, cur_sum, v)
        cur_sum -= ability[i][idx]
        v[i] = 0

def solution(ability):
    answer = 0
    
    v = [0] * len(ability)
    dfs(ability, 0, 0, v)
    answer = max_sum
    
    return answer


    # import itertools


# def solution(ability):
#     answer = 0
#     e = len(ability[0])
#     s = len(ability)

#     for comb in list(itertools.permutations(range(s), e)):
#         answer = max(answer, sum([ability[c][i] for i, c in enumerate(comb)]))
#     return answer


# print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))