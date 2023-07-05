# array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성하는 문제. 
# 최빈값이 여러 개면 -1을 return 합니다.

# 내 풀이
def solution(array):
    arr =[]
    li = list(set(array))    # li = [1,2,3,4]
    for i in li:
        arr.append(array.count(i))  # arr = [1,1,3,1]
        
    answer = -1
    if arr.count(max(arr)) == 1:
        return li[arr.index(max(arr))]
    return answer


# 다른사람 풀이2
# 하나씩 지우면서 마지막에 남는것을 리턴
# 최빈값이 여러개라면 array에서 숫자가 남으므로 -1을 리턴
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1
  
