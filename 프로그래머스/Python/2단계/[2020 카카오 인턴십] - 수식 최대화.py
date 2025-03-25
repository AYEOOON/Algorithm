from itertools import permutations
import re

def solution(expression):
    answer = 0
    
    # 수식에서 연산자(+, -, *)를 추출하여 리스트에 저장
    op = re.findall(r"[+\-\*]", expression)
    
    # 수식에서 숫자들만 분리하여 리스트로 저장
    nums = re.split(r"[+\-\*]", expression)
    
    # 가능한 연산자들의 모든 순열을 생성하여 저장
    ops = list(permutations(op, len(op)))
    
    # 연산자 우선순위 순열에 대해 계산을 시작
    for op_list in ops:
        # 숫자와 연산자 목록을 복사하여 작업을 시작
        tmp_nums = nums[:]
        tmp_ops = op[:]

        # 각 연산자 순열에 대해 계산 수행
        for o in op_list:
            i = 0
            # 숫자와 연산자가 2개 이상 남아 있을 때 연산 수행
            while(i < len(tmp_nums) - 1):
                # 현재 연산자가 op_list에서의 연산자와 일치하면 연산을 수행
                if(tmp_ops[i] == o):
                    a = int(tmp_nums[i])
                    b = int(tmp_nums[i+1])
                    
                    # 연산자에 맞는 연산 수행 후 결과 저장
                    if o == '-':
                        tmp_nums[i] = a - b
                    elif o == '+':
                        tmp_nums[i] = a + b
                    elif o == '*':
                        tmp_nums[i] = a * b
                    
                    # 사용된 숫자와 연산자는 리스트에서 제거
                    tmp_nums.pop(i+1)
                    tmp_ops.pop(i)
                else:
                    i += 1

        # 계산된 결과 중 가장 큰 값 업데이트
        answer = max(answer, abs(int(tmp_nums[0])))

    # 가장 큰 계산 결과 반환
    return answer



# 다른사람 풀이
def solution(expression):
    # 생각해보면 3가지 종류의 연산은 6가지의 경우만 나온다!!!!!!!
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    # 결과를 저장할 리스트
    answer = []
    
    # 각 연산자 우선순위 조합에 대해 계산을 수행
    for op in operations:
        # 현재 연산자 우선순위에서 첫 번째와 두 번째 연산자 추출
        a = op[0]
        b = op[1]
        
        # 연산된 결과를 저장할 임시 리스트
        temp_list = []
        
        # 수식을 첫 번째 연산자(a) 기준으로 분할
        for e in expression.split(a):
            # 두 번째 연산자(b) 기준으로 다시 분할하고 각 부분에 괄호 추가
            temp = [f"({i})" for i in e.split(b)]
            # 괄호가 추가된 부분을 다시 하나의 문자열로 결합하여 temp_list에 추가
            temp_list.append(f'({b.join(temp)})')
        
        # 첫 번째 연산자(a) 기준으로 다시 결합하고, eval()로 계산하여 절댓값을 구해 answer에 추가
        answer.append(abs(eval(a.join(temp_list))))
    
    # 계산된 결과 중 가장 큰 값을 반환
    return max(answer)
