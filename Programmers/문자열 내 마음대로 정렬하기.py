def solution(strings, n):
    strings.sort()
    strings.sort(key=lambda element: element[n])
    return strings