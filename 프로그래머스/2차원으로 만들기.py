# 정수 배열 num_list와 정수 n이 매개변수로 주어집니다. 
# num_list를 다음 설명과 같이 2차원 배열로 바꿔 return하도록 solution 함수를 완성해주세요.


# 내 풀이
# list를 np.array를 사용하여 배열 형태로 바꿔주고, 그걸 다시 tolist()를 사용하여 list형태로 바꿔줌

import numpy as np

def solution(num_list, n):
    return (np.array(num_list).reshape((len(num_list) // n ,n))).tolist() 
  
  
# 다른사람 풀이

def solution(num_list, n):
    return [num_list[ix-n:ix] for ix in range(n, len(num_list)+1, n)]
