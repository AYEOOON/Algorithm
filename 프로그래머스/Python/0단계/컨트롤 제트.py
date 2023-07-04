# "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다.
# 숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.
# 스택이라는 개념을 이용하여 푼 문제
# 결과값이 음수가 올 수 있어 try~exept를 사용
# https://chan-lab.tistory.com/30
# 풀지못함


# 풀이1

def solution(s):
    stack = []
    
    for num in s.split():             # split()함수를 이용하여 문자열을 리스트에 담음
        try:
            stack.append(int(num))
        except:                      # 데이터"z"가 들어오면 stack에서 pop함수를 이용하여, 마지막 것부터 꺼냄
            if stack: 
                stack.pop()
    return sum(stack)
        
    
    
# 풀이2

def solution(s):
    answer = 0
    for i in range(len(s := s.split(" "))):
        answer += int(s[i]) if s[i] != "Z" else -int(s[i-1])
    return answer
