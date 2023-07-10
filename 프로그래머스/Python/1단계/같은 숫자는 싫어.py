# 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.
# arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.


# 내 풀이
def solution(arr):
    answer =[arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer


# 다른사람 풀이
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue  # [-1]을 통해 비교하면 empty array일 때 인덱싱오류가나서 [-1:]를 통해 리스트를 만들어 비교
        a.append(i)
    return a
