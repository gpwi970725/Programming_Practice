def solution(a, b):
    week = {'0':'THU', '1':'FRI', '2':'SAT', '3':'SUN', '4':'MON', '5':'TUE', '6':'WED'}
    month = {'1':31, '2':29, '3':31, '4':30, '5':31, '6':30, '7':31, '8':31, '9':30, '10':31, '11':30, '12':31}
    
    day = b
    if str(a) is not '1':
        for i in range(1, int(a)):
            day = day + month[str(i)]
    
    answer = week[str(day%7)]
    
    return answer


a = 5
b = 24
print(solution(a, b))
