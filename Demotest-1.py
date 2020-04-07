def solution(v):
    x, y = list(), list()
    
    for i in range(3):
        temp = v[i][0]
        x.remove(temp) if temp in x else x.append(temp)
        temp = v[i][1]
        y.remove(temp) if temp in y else y.append(temp)

    return x+y


v = [[1, 1], [2, 2], [1, 2]]

print(solution(v))
