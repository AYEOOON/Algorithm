# 내 풀이
def solution(lottos, win_nums):
    arr = []   # 구매한 로또 번호중 알아볼 수 없는 번호와 맞춘 번호를 구한다. 

    for i in range(len(lottos)):
        if lottos[i] in win_nums or lottos[i] == 0:
            arr.append(lottos[i])
    a = arr.count(0)
    b = len(arr) - a  
  
    # 맞춘 번호 최대값 = 맞춘 번호 + 알아볼 수 없는 번호의 개수 ( 알아볼 수 없는 번호가 모두 맞았다고 가정 )
    # 맞춘 번호 최소값 = 맞춘 번호 ( 알아볼 수 없는 번호가 모두 틀렸다고 가정 )
    return [7-(a+b) if a+b > 1 else 6, 7-b if b>1 else 6]  # 맞춘 개수에 따라서 최고 순위와 최저 순위 계산


# 다른사람 풀이
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
