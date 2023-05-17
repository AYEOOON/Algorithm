# 1부터 입력으로 주어진 숫자(예를 들어 8)를 오름차순으로 스택에 push하면서 적절히 pop해 입력으로 주어진 수열 4, 3, 6, 8, 7, 5, 2, 1을 만들면 된다.


# 코드

n = int(input())
stack = []  # 오름차순으로 넣은 스택
result = []  # push,pop 여부에 따른 연산 여부를 +,-로 저장
count = 1
temp = True

for i in range(n):
  num = int(input())
  
  # num이하 숫자까지 스택에 넣기
  while(count <= num):
    stack.append(count)
    result.append("+")
    count += 1

  #num이랑 스택 맨 위 숫자가 동일하다면 제거
  if stack[-1] == num:
    stack.pop()
    result.append("-")
  
  #스택스열을 만들 수 없으므로 NO
  else:
    temp = False
    print("NO")
    break

# 스택 수열을 만들 수 있는지 여부에 따라 출력
if temp == True:
  for i in result:
    print(i)
