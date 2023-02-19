# 머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때, 머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.

# 내 풀이

def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer



# 다른사람 풀이1
# 시간복잡도는 더 긴 풀이이지만 참고할 만 하다. 

def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)
    
  
  
# 다른사람 풀이2

def solution(array, height):
    return sum(1 for a in array if a > height)
