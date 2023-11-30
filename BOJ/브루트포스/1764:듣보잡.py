# 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 
# 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 
# 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.
# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.
# 듣보잡의 수와 그 명단을 사전순으로 출력한다.

# 리스트를 써서 시간 초과가 발생하면 set을 이용하면 된다!

# 내 풀이
# import sys
# input = sys.stdin.readline  # 이게 자꾸 리스트에 '\n'을 집어넣었다.

N,M = map(int,input().split())

no_hear_person = set([])
no_see_person = set([])

cnt = 0

for i in range(N):
  no_hear_person.add(input())
for j in range(M):
  no_see_person.add(input())

two_no = no_hear_person & no_see_person

two_no = sorted(two_no)

print(len(two_no),*two_no,sep='\n')

# 다른사람 풀이
import sys
n, m = map(int, input().split())
nameList = sys.stdin.read().splitlines()
hearset = set(nameList[:n])
seeset = set(nameList[n:])
ret = list(hearset & seeset)
ret.sort()
print(len(ret))
for i in ret:
    print(i)
