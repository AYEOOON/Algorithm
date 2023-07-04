# 3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 3의 배수와 숫자 3을 사용하지 않습니다.
# 10진법	3x 마을에서 쓰는 숫자	10진법	3x 마을에서 쓰는 숫자
# 1	1	6	8
# 2	2	7	10
# 3	4	8	11
# 4	5	9	14
# 5	7	10	16
# 정수 n이 매개변수로 주어질 때, n을 3x 마을에서 사용하는 숫자로 바꿔 return하도록 solution 함수를 완성해주세요.
# 못 푼 문제

# 풀이 1

def solution(n):
    n_list = [i for i in range(1,230)]
    n_list2 = []
    for i in n_list:
        if i%3 != 0 and i%10 != 3 and (i<30 or i >=40) and (i<130 or i >=140):
            n_list2.append(i)

    return n_list2[n-1]
  
  
# 풀이 2 (나도 첨엔 이런 방향..)

def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer
