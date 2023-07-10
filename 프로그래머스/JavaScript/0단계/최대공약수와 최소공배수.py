# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
# 최소공배수 = (n*m)//최대공약수

# 내 풀이
import math
def solution(n, m):
    return[math.gcd(n,m), (n*m)//math.gcd(n,m)]


# 다른사람 풀이(유클리드 호제법)
def gcdlcm(a, b):
    c,d = max(a, b), min(a, b)
    t = 1
    while t>0:
        t = c%d
        c, d = d, t
    answer = [ c, int (a*b/c)]
    return answer


# 다른사람 풀이(람다사용)
def solution(n, m):
    gcd = lambda a,b : b if not a%b else gcd(b, a%b)
    lcm = lambda a,b : a*b//gcd(a,b)
    return [gcd(n, m), lcm(n, m)]
