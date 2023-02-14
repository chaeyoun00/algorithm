def dfs(n, computers, i, v):
    v[i] = 1
    for j in range(n):
        if i != j and computers[i][j] == 1:
            if v[j] == 0:
                dfs(n, computers, j, v)
    return

def solution(n, computers):
    answer = 0
    
    v = [0 for i in range(n)]
    for i in range(n):
        if v[i] == 0:
            dfs(n, computers, i, v)
            answer += 1
            
    return answer