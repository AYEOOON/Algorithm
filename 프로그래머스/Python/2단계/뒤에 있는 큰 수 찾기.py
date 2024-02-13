"""
정수로 이루어진 배열 numbers가 있습니다. 
배열 의 각 원소들에 대해 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수를 뒷 큰수라고 합니다.
정수 배열 numbers가 매개변수로 주어질 때, 모든 원소에 대한 뒷 큰수들을 차례로 담은 배열을 return 하도록 solution 함수를 완성해주세요. 
단, 뒷 큰수가 존재하지 않는 원소는 -1을 담습니다.
"""
"""
처음에 이중 for문을 이용해서 풀었지만, 시간초과로 인해 실패
stack을 이용하여 이전의 수를 저장했다가, 큰 수가 나오면 다시 갱신
"""

# 내 풀이
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i, num in enumerate(numbers):
      # 스택에 들어있는 것은 index, 아직 큰수를 찾지 못한 수로 생각하면 됨
        while(stack and numbers[stack[-1]] < num):  # 스택의 제일 위에 있는 index의 수가 현재 숫자보다 작을때
            a = stack.pop() 
            answer[a] = num
        stack.append(i)
    return answer
