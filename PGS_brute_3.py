from itertools import permutations

def prime_num(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1

def solution(numbers):
    answer = []
    
    number = list(numbers)
    nums = []
    for i in range(1, len(number) + 1):
        nums += list(permutations(number, i))
    nums = [int(("").join(p)) for p in nums]
    nums = list(set(nums))
    
    for i in range(len(nums)):
        if nums[i] <= 1:
            continue
        
        if prime_num(nums[i]) == 1:
            answer.append(nums[i])
            
    return len(set(answer))


print(solution("011"))