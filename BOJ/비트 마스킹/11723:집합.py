# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

# 처음에 리스트로 풀었는데, 시간초과가 계속 떴다. 
# 연산의 수가 3,000,000까지 가능하므로 list에 담기에는 메모리가 부족하다.
# set을 이용해서 다시 풀었는데 시간초과를 해결하지 못했다. 

# 내 풀이
import sys
input = sys.stdin.readline

n = int(input())
S = set()

for cmd in range(n):
  cmd = list(input().split())
  if cmd[0] == 'add':
    if cmd[1] in S:
      pass
    else:
      S.add(cmd[1])

  elif cmd[0] == 'remove':
    if cmd[1] in S:
      S.discard(cmd[1])
    else:
      pass

  elif cmd[0] == 'check':
    if cmd[1] in S:
      print('1')
    else:
      print('0')

  elif cmd[0] == 'toggle':
    if cmd[1] in S:
      S.discard(cmd[1])
    else:
      S.discard(cmd[1])
      
  elif cmd[0] == 'all':
    S = set([str(i) for i in range(1,21)])

  elif cmd[0] == 'empty':
    S = set([])


# 다른사람 풀이
import sys
input = sys.stdin.readline
m = int(input())
s = set()
for _ in range(m):
  arr = list(input().split())
  c = arr[0]
  if c == 'add':
    s.add(int(arr[1]))
  elif c == 'remove':
    try:
      s.remove(int(arr[1]))
    except:
      pass
  elif c == 'check':
    if int(arr[1]) in s:
        print(1)
    else:
      print(0)
  elif c == 'toggle':
    if int(arr[1]) in s:
      s.remove(int(arr[1]))
    else:
      s.add(int(arr[1]))
  elif c == 'all':
    s = set([i for i in range(1,21)])
  else:
    s = set()
