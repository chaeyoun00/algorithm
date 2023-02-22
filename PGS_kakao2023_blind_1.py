def solution(today, terms, privacies):
    answer = []
    
    days = today.split(".")
    term = {}
    for i in terms:
        month = i.split(" ")
        term[month[0]] = month[1]
    
    for i in range(len(privacies)):
        inform = privacies[i].split(" ")
        day = inform[0].split(".")
        
        cal = term[inform[1]]
        day[0] = str(int(day[0]) + (int(cal) // 12))
        if int(day[1]) + (int(cal) % 12) > 12:
            day[0] = str(int(day[0]) + 1)
            day[1] = str(int(day[1]) + (int(cal) % 12) - 12)
        else:
            day[1] = str(int(day[1]) + (int(cal) % 12))
        
        if int(day[2]) - 1 == 0:
            if int(day[1]) == 1:
                day[0] = str(int(day[0]) - 1)
                day[1] = '12'
                day[2] = '28'
            else: 
                day[1] = str(int(day[1]) - 1)
                day[2] = '28'
        else:
            day[2] = str(int(day[2]) - 1)
            
        if int(day[0]) < int(days[0]):
            answer.append(i + 1)
        elif int(day[0]) == int(days[0]):
            if int(day[1]) < int(days[1]):
                answer.append(i + 1)
            elif int(day[1]) == int(days[1]):
                if int(day[2]) < int(days[2]):
                    answer.append(i + 1)
    return answer


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))