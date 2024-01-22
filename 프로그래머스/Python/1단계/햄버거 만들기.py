"""
상수가 일하는 가게는 정해진 순서(아래서부터, 빵 – 야채 – 고기 - 빵)로 쌓인 햄버거만 포장을 합니다. 
상수는 손이 굉장히 빠르기 때문에 상수가 포장하는 동안 속 재료가 추가적으로 들어오는 일은 없으며, 재료의 높이는 무시하여 재료가 높이 쌓여서 일이 힘들어지는 경우는 없습니다.

예를 들어, 상수의 앞에 쌓이는 재료의 순서가 [야채, 빵, 빵, 야채, 고기, 빵, 야채, 고기, 빵]일 때, 상수는 여섯 번째 재료가 쌓였을 때, 세 번째 재료부터 여섯 번째 재료를 이용하여 햄버거를 포장하고, 아홉 번째 재료가 쌓였을 때, 두 번째 재료와 일곱 번째 재료부터 아홉 번째 재료를 이용하여 햄버거를 포장합니다.
즉, 2개의 햄버거를 포장하게 됩니다.

상수에게 전해지는 재료의 정보를 나타내는 정수 배열 ingredient가 주어졌을 때, 상수가 포장하는 햄버거의 개수를 return 하도록 solution 함수를 완성하시오.
"""
"""
배열을 원소를 하나씩 받아와서 마지막 4개의 원소가 1231인지 확인
확인이 되면 마지막 4개의 원소 삭제 후, 햄버거 만든 개수 1 추가
"""

# 내 풀이
def solution(ingredient):
    hamberger = 0
    temp = []
    idx = 0
    a = 0
    b = 0
    
    while(a == 0):
        b = len(ingredient)
        for i in range(idx,len(ingredient)):
            if ingredient[i:i+4] == [1,2,3,1]:
                del ingredient[i:i+4]
                idx = i-3
                hamberger += 1
                break
            
        if i+1 == b:
            a = 1
            
    return hamberger


# 다른사람 풀이
def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for i in range(4):
                s.pop()
    return cnt
