# array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성하는 문제. 
# 최빈값이 여러 개면 -1을 return 합니다.
# 문제를 풀지 못함


# 풀이1

def solution(array: list) -> int:
    dict = {}

    # for 반복문으로 입력 list 순회
    for num in array:
        # 딕셔너리에 현재 값이 할당되있지 않다면 1 할당
        if num not in dict:
            dict[num] = 1
        # 그렇지 않을 시, 증감
        else:
            dict[num] += 1
            
    # 딕셔너리의 벨류값 기준으로 desc 정렬
    result = sorted(dict.items(), key=lambda x: x[-1], reverse=True)
    
    if len(result) <= 1:
        return result[0][0]
    # 최빈값이 여러개면, -1 반환
    return result[0][0] if result[0][-1] != result[1][-1] else -1

if __name__ == '__main__':
    print(solution([1, 2, 3, 3, 3, 4]))  # 3
    print(solution([1, 1, 2, 2]))  # -1
    print(solution([1]))  # 1


# 풀이2

def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1
  
