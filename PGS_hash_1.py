def solution(nums):
    answer = 0
    
    pocketmons = len(nums) // 2
    arr = set(nums)
    
    if len(arr) < pocketmons:
        answer = len(arr)
    else:
        answer = pocketmons
    
    return answer

print(solution([3,3,3,2,2,4]))


# def solution(ls):
#     return min(len(ls)/2, len(set(ls)))