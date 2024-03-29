# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 
# 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.
# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
# 첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.

# 분해합이 주어졌을 때 그 생성자를 역으로 찾을 수는 없다.(생성자가 여러개일수도 있기때문)
# N의 분해합은 무조건 N보다 크기 때문에 1부터 (N-1)까지 분해합을 찾는 함수를 돌리면서 가장 처음 N의 분해합이 구해지면 그 때의 생성자가 N의 가장 작은 생성자이므로 출력한다. 
# (N-1)까지 분해합이 구해지지 않으면 0을 출력


# 풀이
n = int(input())  # 분해합을 입력값으로 받음

for i in range(1, n+1):   # 해당 분해합의 생성자 찾기
    num = sum((map(int, str(i))))  # i의 각 자릿수를 더함
    num_sum = i + num  # 분해합 = 생성자 + 각 자릿수의 합
    # i가 작은 수부터 차례로 들어가므로 처음으로 분해합과 입력값이 같을때가 가장 작은 생성자를 가짐
    if num_sum == n:
        print(i)
        break
    if i == n:  # 생성자 i와 입력값이 같다는 것은 생성자가 없다는 뜻
        print(0)
