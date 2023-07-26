# 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 
# 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 
# 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 
# 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 
# 여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.
# 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 
# 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 


# 내 풀이
N = int(input())

VPS = []
for i in range(N):
  VPS.clear()
  check = 0
  PS = input()
  for j in PS:
    if j == '(': 
      VPS.append(j)
    else:
      if len(VPS) == 0:
        check = 1
        break
      else: VPS.pop()
  if len(VPS) == 0 and check == 0:
    print('YES')
  else: print("NO")


# 다른사람 풀이
import sys
vps = sys.stdin.readlines()[1:]

for v in vps:
	v = v.rstrip()
	while '()' in v:
		v = v.replace('()', '')  # 괄호 쌍을 찾아 모두 공백으로 만듦
	
	if v:
		print('NO')
	else:
		print('YES')
