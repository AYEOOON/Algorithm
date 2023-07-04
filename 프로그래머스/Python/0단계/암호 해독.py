# 문자열 cipher와 정수 code가 매개변수로 주어질 때 해독된 암호 문자열을 return하도록 solution 함수를 완성해주세요.
# 암호화된 문자열 cipher를 주고받습니다.
# 그 문자열에서 code의 배수 번째 글자만 진짜 암호입니다.
# 풀지못함
# 'join'을 쓰게 되면 복잡도가 상승하게 된다.


# 풀이1

def solution(cipher, code):
    answer = cipher[code-1::code]   # 'join'을 쓰게 되면 복잡도가 상승하게 된다.
        
    return answer
  
# 더 줄인 풀이

def solution(cipher, code):

    return cipher[code-1::code]
  
  
# 풀이2

ef solution(cipher, code):
    return ''.join(cipher[i] for i in range(code-1,len(cipher),code))
