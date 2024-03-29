# 교수님이 만들 자동 응답 챗봇의 응답을 출력하는 프로그램을 만드는 문제
# 교수님이 출력을 원하는 재귀 횟수 N이 주어지면, 출력 예시를 보고 재귀 횟수에 따른 챗봇의 응답을 출력한다.  
# 처음에 무한루프가 발생하여 당황했지만, return을 추가하여 해결할 수있었다.

# 내 풀이
 
import sys

def func(N):
  print("____"*N + "재귀함수가 뭔가요?")
  if N==end:
    print("____"*N + "재귀함수는 자기 자신을 호출하는 함수라네")
    print("____"*N + "라고 답변하였지.")
    return

  print("____"*N + "잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
  print("____"*N + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
  print("____"*N + "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.")
  func(N+1)
  print("____"*N + "라고 답변하였지.")

end = int(sys.stdin.readline())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
func(0)


# 다른사람 풀이
def f(i):
	if i>n :
		return
	print('____'*i + '"재귀함수가 뭔가요?"')
	if i==n :
		print('____'*i + '"재귀함수는 자기 자신을 호출하는 함수라네"')
	else :
		print('____'*i + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
		print('____'*i + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
		print('____'*i + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
	f(i+1)
	print('____'*i + '라고 답변하였지.')

n = int(input())
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
f(0)
