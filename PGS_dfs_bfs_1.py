cnt = 0

def dfs(total, idx, numbers, target):
    global cnt
    
    if idx == len(numbers):
        if total == target:
            cnt += 1
        return
    
    total += numbers[idx]
    dfs(total, idx + 1, numbers, target)
    total -= numbers[idx] * 2
    dfs(total, idx + 1, numbers, target)


def solution(numbers, target):
    answer = 0
    
    dfs(0, 0, numbers, target)
    answer = cnt
    
    return answer


# def solution(numbers, target):
#     print(numbers, target)
#     if not numbers and target == 0 :
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


print(solution([4, 1, 2, 1], 4))