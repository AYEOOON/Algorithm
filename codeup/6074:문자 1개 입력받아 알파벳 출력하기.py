# 영문 소문자(a ~ z) 1개가 입력되었을 때, a부터 그 문자까지의 알파벳을 순서대로 출력해보자.



c = ord(input())    # 알파벳 문자 a의 정수값은 ord('a')로 알아낼 수 있다.
t = ord('a')
while t<=c :
  print(chr(t), end=' ')
  t += 1
