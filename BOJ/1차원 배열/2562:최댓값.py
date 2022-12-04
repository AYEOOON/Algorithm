# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.


# 내 풀이
arr = []

for i in range(9):   # 9개의 수를 for문으로 입력받음
  arr.append(int(input()))
print(max(arr), arr.index(max(arr))+1)  # index 함수의 순서는 0번째부터 시작하기 떄문에 1을 더해주었다. 


# 9개의 숫자를 입력받기 위한 리스트를 만들기 위해 리스트 컴프리헨션으로 작성할 수 있다. 
a = [int(input()) for _ in range(9)]


# 다른사람 풀이
x=[int(input()) for a in range(9)]
print(max(x),x.index(max(x))+1)
