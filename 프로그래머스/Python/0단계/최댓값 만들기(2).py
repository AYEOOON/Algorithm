# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.




# 내 풀이

def solution(numbers):
    numbers.sort(reverse = True)
    return max(numbers[0]*numbers[1], numbers[-1]*numbers[-2])
  
  
# 다른사람 풀이

from itertools  import combinations as comb

def solution(numbers):
    an_list=[]
    for i,j in comb(numbers,2):
        an_list.append(i*j)
    return max(an_list)
