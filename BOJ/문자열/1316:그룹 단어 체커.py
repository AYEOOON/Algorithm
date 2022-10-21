# 각 문자가 연속해서 나타나는 경우를 뜻하는 그룹단어를 N개 입력받아 그룹 단어의 개수를 출력하는 프로그램을 작성하는 문제
# 입력된 문자열을 검사하는데, 특정 문자 다음에 다른 문자가 나올 경우 문자열에서 그 글자 다음부터 끝까지 검사하여 이상없으면 그룹단어로 카운트하였다.

# 내 풀이


N = int(input())
group_word = 0

for _ in range(N):
  word = input()
  error = 0
  for index in range(len(word)-1):       # 인덱스 범위 생성: 0부터 단어개수 -1까지
    if word[index] != word[index+1]:     # 연달은 두 문자가 다를 때
      new_word = word[index+1:]          # 현재 글자 이후 문자열을 새로운 단어로 생성
      if new_word.count(word[index]) > 0: # 남은 문자열에서 현재 글자가 있었다면
        error += 1    # error에 1씩 증가
  if error == 0:      # error가 0이면 그룹단어
    group_word += 1
print(group_word)
      
  
# 다른 사람 풀이

result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)
