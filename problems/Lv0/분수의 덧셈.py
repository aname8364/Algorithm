import math

def solution(numer1, denom1, numer2, denom2):
    
    x = denom1 * denom2
    y = (numer1 * denom2) + (numer2 * denom1)
    z = math.gcd(x, y)
    
    answer = [y//z, x//z]
    return answer