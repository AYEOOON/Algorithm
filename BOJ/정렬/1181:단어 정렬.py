# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 길이가 짧은 순으로 정렬하는 프로그램을 작성하는 문제
# 길이가 같으면 사전 순으로 정열한다. 단어가 중복되어 출력되면 안됌
# sort는 문자열도 정열해주는 것을 이용하여 문제를 풀었다. 


# 내 풀이

import sys
strip=sys.stdin.readline

n = int(input())
word = []

for i in range(n):
  word.append(strip())

set_word = set(word)
word = list(set_word)
word.sort()
word.sort(key = len)

for i in word:
  print(i,end='')
