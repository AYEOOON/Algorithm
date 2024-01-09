"""
 진영 주식회사는, 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다. 
 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.

이러한 조건을 만족시키면서, 진영 주식회사가 이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원수를 구하는 프로그램을 작성하시오.

"""

# 내 풀이
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
  N = int(input())
  jiwon = [list(map(int, input().split())) for _ in range(N)]
  jiwon_sort = sorted(jiwon)  # 지원자를 정렬함으로써 서류심사 성적을 비교대상에서 제외한다. 
  cnt = 1
  top = 0
  for k in range(1, len(jiwon_sort)):
    if jiwon_sort[k][1] < jiwon_sort[top][1]:  # i번째 사람의 면접 성적이 0~(i~1)번째 사람들의 모든 면접 성적보다 순위가 높으면 채용
      top = k
      cnt += 1
    

  print(cnt)

# 다른사람 풀이
import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t):
    n = int(input())
    grade = [0]*(n+1)
    for i in range(n):
        a, b = map(int,input().split())
        grade[a] = b
    # 높은 순위 저장
    top = grade[1]
    # 작은 수가 높은 순위
    for i in range(2, n+1):
        if grade[i] < top:
            # 순위가 높으면 top을 높은 순위로 바꾸기
            top = grade[i]
        else:
            # 순위가 낮으면 개수 감소
            n -= 1
    print(n)
