def solution(answers):
    answer = []
    math = [0, 0, 0]
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    

    for i in range(len(answers)):
        if answers[i] == p1[i % len(p1)]:
            math[0] = math[0] + 1
        if answers[i] == p2[i % len(p2)]:
            math[1] += 1
        if answers[i] == p3[i % len(p3)]:
            math[2] += 1
    
    if math.count(max(math)) > 1:
        for i in range(len(math)):
            if math[i] == max(math):
                answer.append(i + 1)
    else:
        answer.append(math.index(max(math)) + 1)
        
    return answer


print(solution([1,3,2,4,2]))