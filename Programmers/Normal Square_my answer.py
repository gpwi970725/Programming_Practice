from math import gcd
    
def solution(w,h):
    gcd_wh = gcd(w,h)
    w_quo, h_quo = int(w/gcd_wh), int(h/gcd_wh)

    return (w*h)-((w_quo+h_quo-1)*gcd_wh)


w = 8
h = 12
print(solution(w,h))


"""
The GCD is written as follows.
I used the Euclidean remedy.

'''
def euclidean(x,y):
    if x<y:
        temp = y
        y = x
        x = temp
    while y:
        x, y = y, x%y
    return x
'''

I can change the code like this.

'''
def solution(w,h): return w*h-w-h+gcd(w,h)
'''
"""
