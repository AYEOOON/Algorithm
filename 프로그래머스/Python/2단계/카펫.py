"""
카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.
Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 
카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.
"""
# 1. yellow의 약수를 구함
# 2. 약수들의 처음과 끝, 투포인터를 이용해 둘을 곱한 것이 brown과 yellow의 합과 같으면 +2를 함

# 내 풀이
def solution(brown, yellow):
    arr = []
    hap = brown+yellow

    for i in range(1,yellow+1):
        if yellow%i == 0:
            arr.append(i)
            
    arr.sort(reverse=True)
    
    end = len(arr)-1
    for srt in range(len(arr)):
        if (arr[srt]+2)*(arr[end]+2) == hap:
            return [arr[srt]+2,arr[end]+2]
        
        else:
            end -= 1


# 다른사람 풀이
# 제 내용 중 "테두리 1줄은 갈색" <- 갈색은 한줄뿐이다. 
# 따라서, 2*(노랑의 가로 + 노랑의 세로) + 4 = 갈색의 총 개수 || 또한 가로가 세로보다 길어야 하기 때문에 약수들을 찾을 때
# 0.5제곱근으로 범위 제한하고 해당 약수로 다시 모수를 나눠서 구해지는 대칭 약수를 구할 필요X
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]
