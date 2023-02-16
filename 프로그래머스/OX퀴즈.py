# 덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다. 
# 수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.
# quiz) ["3 - 4 = -3", "5 + 6 = 11"],   result) ["X", "O"]
# 정답 근처에서 못풂


# 풀이1 

def solution(quiz):
    answer = []
    for i in quiz:
        calc = i.split('=')
        answer.append('O' if eval(calc[0]) == eval(calc[1]) else 'X')
    return answer
  
  
  
# 풀이2

def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]    
