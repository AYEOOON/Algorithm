"""
비트연산자 XOR을 사용해서 풀이한 방법이다. 비트연산으로 풀거라고 생각도 못했는데..!
어떤 원리냐면, 같은값 2개와 다른값 1개를 xor 연산시키면 다른값 1개가 반환된다는 원리이다.
a ^ a = 0
a ^ a ^ b = b
"""

def solution(v):
    x = v[0][0] ^ v[1][0] ^ v[2][0]
    y = v[0][1] ^ v[1][1] ^ v[2][1]
    return x,y
