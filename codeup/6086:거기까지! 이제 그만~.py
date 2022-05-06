# 1, 2, 3 ... 을 순서대로 계속 더해 합을 만드는데, 그 합이 입력한 정수보다 작을 동안만 계속 더하는 프로그램을 작성해보자.

a = int(input())
total = 0
i = 1

while (total < a):
    total = total + i
    i = i + 1
print(total)
