# 자연수 N과 M이 주어졌을 때, 1부터 N까지 자연수 중에서 중복없이 M개를 고른 수열을 모두 반환
# 첫째 줄에 자연수 N과 M이 주어진다. 
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야한다. 
# https://velog.io/@yusuk6185/%EB%B0%B1%EC%A4%80-15649-N%EA%B3%BC-M-1-%ED%8C%8C%EC%9D%B4%EC%8D%AC-with-%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9

# 풀이
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

def func():
  if(len(arr) == m):  # 배열의 길이가 m이 되는 경우 해당 리스트 내의 숫자들을 join 메서드를 활용하여 출력 후 해당 dfs 종료
    print(''.join(map(str,arr)))
    return 

  # for 문으로 반복
  for i in range(1,n+1): 
    if i not in arr:  # 만약 i가 리스트 s안에 존재하지 않는다면 삽입을 해주고 함수를 호출한다.
      arr.append(i)
      func()
      arr.pop()  # 해당 함수가 출력 된 후 가장 뒤에 들어온 i를 pop하여 제거해준다

func()
