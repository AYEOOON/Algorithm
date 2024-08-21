"""
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.
"""

# 내 풀이
def solution(arr1, arr2):
    x,y,z = len(arr2[0]), len(arr1), len(arr1[0])

    arr = [[0]*x for _ in range(y)]
    
    for i in range(y):
        for j in range(x):
            sum = 0 
            for k in range(z):
                sum += arr1[i][k] * arr2[k][j]
            arr[i][j] = sum
    
    return arr

# 다른사람 풀이1
# 배열에 0이 아닌 추가적인 배열에 값을 저장하고, 다시 다른 배열에 추가하는 방식
def productMatrix(A, B):
    answer = []

    for i in range(len(A)):
        arr = []
        for j in range(len(B[0])):
            tmp = 0
            for k in range(len(A[0])):
                tmp += A[i][k] * B[k][j]
            arr.append(tmp)
        answer.append(arr)

    return answer


# 다른사람 풀이2
# numpy는 가능한 곳이 있고, 안되는 곳이 있다! 주의!
import numpy as np
def productMatrix(A, B):

    return (np.matrix(A)*np.matrix(B)).tolist()
