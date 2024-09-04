"""
이차원 정수 배열 arr이 매개변수로 주어집니다. 
arr의 행의 수가 더 많다면 열의 수가 행의 수와 같아지도록 각 행의 끝에 0을 추가하고, 
열의 수가 더 많다면 행의 수가 열의 수와 같아지도록 각 열의 끝에 0을 추가한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.
"""
# 이번엔 다른사람 풀이와 내 풀이가 같다!!

# 내 풀이
def solution(arr):
    n = max(len(arr), len(arr[0]))
    for i in range(n):
        if len(arr[i]) < n:
            for j in range(n-len(arr[i])):  # 0의 갯수가 모자란 만큼 반복
                arr[i].append(0)
        elif len(arr) < n:
            arr.append([0]*n)
            
    return arr
