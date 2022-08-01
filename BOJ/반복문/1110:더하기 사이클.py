# N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.
# 첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.
# 첫째 줄에 N의 사이클 길이를 출력한다.


# 내 풀이

N = int(input())  #입력받은 값을 int로 바꿈
num = N           #변하는 값
count = 0         #몇 번 사이클인지
 
while True:
    a = num//10
    b = num %10
    c = (a+b)%10
    num = (b*10) + c
    count += 1
    if(num == N):
        break
 
print(count)



# 다른사람 풀이
