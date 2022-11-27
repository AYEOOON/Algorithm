# https://www.acmicpc.net/problem/25501
# 팰린드롬이란, 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때가 같은 문자열을 말한다.
# 위 링크 코드의 isPalindrome 함수는 주어진 문자열이 팰린드롬이면 1, 팰린드롬이 아니면 0을 반환하는 함수다.
# isPalindrome 함수를 이용하여 어떤 문자열이 팰린드롬인지 여부를 판단하려고 한다. 
# 문자열 $S$를 isPalindrome 함수의 인자로 전달하여 팰린드롬 여부를 반환값으로 알아낼 것이다. 더불어 판별하는 과정에서 recursion 함수를 몇 번 호출하는지 셀 것이다.
# 함수의 반환값과 recursion 함수의 호출 횟수를 구해보자.


# 내 풀이

import sys
input = sys.stdin.readline

def recursion(s, l, r):
    global cnt # 함수 내에서 전역 변수로 cnt를 활용하기 위해 global로 명시해준다.
    cnt += 1
    
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for _ in range(int(input())):
    cnt = 0
    print(isPalindrome(input().rstrip()), cnt)
