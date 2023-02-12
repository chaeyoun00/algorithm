def pop_stack(stack):
    while len(stack) > 0:
        num = stack.pop()
        if num == 0: return "RR"
        if num == 3: return "rr"
    return "Rr"

def solution(queries):
    answer = []
    
    for n, p in queries:
        stack = []
        p -= 1
        while n > 1:
            stack.append(p % 4)
            n -= 1
            p //= 4
        
        answer.append(pop_stack(stack))
    
    return answer


print(solution([[3, 1], [2, 3], [3, 9]]))