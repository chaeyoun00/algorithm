def solution(id_list, report, k):
    answer = []
    
    id = {}
    id_stop = {}
    for ids in id_list:
        id[ids] = []
        id_stop[ids] = 0
    
    report = list(set(report))
    for i in report:
        id_report = i.split(" ")
        id[id_report[0]].append(id_report[1])
        id_stop[id_report[1]] += 1
    
    for ids in id_list:
        cnt = 0
        for i in id[ids]:
            if id_stop[i] >= k:
                cnt += 1
        answer.append(cnt)
        
    return answer


# def solution(id_list, report, k):
#     answer = [0] * len(id_list)    
#     reports = {x : 0 for x in id_list}

#     for r in set(report):
#         reports[r.split()[1]] += 1

#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1

#     return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))