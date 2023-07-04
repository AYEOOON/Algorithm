# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

# 내 풀이
def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i]%divisor==0:
            answer.append(arr[i])
    if len(answer) ==0:
        answer.append(-1)
    return sorted(answer)
  

# 개선한 내풀이(처음 시도한 풀이)
def solution(arr, divisor):
    return sorted([i for i in arr if i%divisor==0 ]) or [-1]   # or을 생각하지 못해서 저렇게 어렵게 풀었다니..


# 다른사람 풀이
def solution(arr, divisor):
    arr = [x for x in arr if x % divisor == 0];
    arr.sort();
    return arr if len(arr) != 0 else [-1];
