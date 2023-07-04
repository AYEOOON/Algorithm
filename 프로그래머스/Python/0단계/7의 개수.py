# 정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.
# 리스트를 문자열로 만드는 방법을 너무 복잡하게 생각한 것 같다. 

# 내 풀이

def solution(array):
    arr = ''.join(map(str, array))
    return arr.count('7')
  
  
# 다른사람 풀이

def solution(array):
    return str(array).count('7')
