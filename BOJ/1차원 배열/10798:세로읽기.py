# 글자들은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’이다. 영석이는 칠판에 글자들을 수평으로 일렬로 붙여서 단어를 만든다.
# 세로로 읽은 순서대로 글자들을 출력하는 프로그램을 작성하시오.


# 내 풀이
import sys
sys.stdin.readline

word = [input() for _ in range(5) ]   # 2차원배열로 안풀어도 됨

for i in range(15):  # 단어의 최대 길이는 15이다. 
  for j in range(5):  # 글자를 출력하기위한 반복문은 5이다. 
    if i<len(word[j]):  # i가 단어길이보다 작으면 인덱스 범위 안에 있으므로 출력할 수 있다.
      print(word[j][i], end ='')


# 다른사람 풀이
li = ['']*75
for i in range(5):
    S = input()
    idx = i
    for c in S:
        li[idx] = c
        idx += 5
print(''.join(li))
