def solution(array, commands):
    answer = []
    
    for command in commands:
        answer.append(sorted(array[command[0] - 1:command[1]])[command[2] - 1])
    
    return answer


# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))