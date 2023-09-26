import math

def geron(a,b,c):

    s = (a+b+c/2)
    plo = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return plo

