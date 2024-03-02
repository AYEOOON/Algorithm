"""
길이가 같은 배열 A, B 두개가 있습니다. 각 배열은 자연수로 이루어져 있습니다.
배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다. 
이러한 과정을 배열의 길이만큼 반복하며, 두 수를 곱한 값을 누적하여 더합니다. 
이때 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다. (단, 각 배열에서 k번째 숫자를 뽑았다면 다음에 k번째 숫자는 다시 뽑을 수 없습니다.)
배열 A, B가 주어질 때 최종적으로 누적된 최솟값을 return 하는 solution 함수를 완성해 주세요.
"""
"""
1. A는 오름차순으로 정렬하고, B는 내림차순으로 정렬
2. 각 인덱스에 있는 것들을 묶어 곱한 뒤 배열에 넣음
3. 배열의 합을 리턴
"""

# 내 풀이
def solution(A,B):
    A = sorted(A)
    B = sorted(B, reverse = True)
    arr = []
    for i in range(len(A)):  # 리스트 두개를 한쌍으로 묶는 함수가 기억이 나지 않았다. 
        arr.append(A[i]*B[i])
    return sum(arr)

# 다른사람 풀이(zip)
def getMinSum(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])  # zip() 내장함수로 데이터 엮기


# 다른사람 풀이(lambda)
def getMinSum(A,B):
    return sum(map(lambda a,b : a*b, sorted(A), sorted(B, reverse=True))) 
