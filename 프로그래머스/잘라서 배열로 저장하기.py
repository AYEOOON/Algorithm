# 문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

# 내 풀이

def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):     # 0부터 len(my_str)까지 n만큼씩의 간격을 설정하는 것이 중요하다.
        answer.append(my_str[i:i+n])

    return answer
  
  
  
  
# 다른사람 풀이

def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]  # 슬라이싱은 초과해도 에러가 나지 않음
