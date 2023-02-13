from collections import Counter

def solution(participant, completion):
    answer = ''
    
    p_dict = Counter(participant)
    c_dict = Counter(completion)
    
    answer = list(p_dict - c_dict)[0]
    
    return answer



# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#
#     return participant[len(participant)-1]


# def solution(participant, completion):
#     answer = ''
#     temp = 0

#     dic = {}
#     for part in participant:
#         dic[hash(part)] = part
#         temp += hash(part)
#     print(dic)
#     print(temp)
#     for com in completion:
#         temp -= hash(com)
#     answer = dic[temp]

#     return answer


print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))