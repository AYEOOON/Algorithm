# 정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 없으면 -1을 return 하도록 solution 함수를 완성해보세요.
# find()함수를 쓰는게 까다로웠음
# find(): 찾는 문자가 없는 경우에 -1을 출력한다


# 내 풀이

def solution(num, k):
    arr = str(num)
    if str(k) in arr:        # 정수는 차례대로 하나씩 셀 수 없기 때문에 리스트나 문자열 등으로 바꿔야함
        return (arr.find(str(k)))+1     # '변수. find(찾을 문자)' 
    else:
        return -1
      
      
# 다른사람 풀이1

def solution(num, k):
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1
  
  
# 다른사람 풀이2

def solution(num, k):
    for i, n in enumerate(str(num)):  # enumerate() 함수는 기본적으로 인덱스와 원소로 이루어진 튜플(tuple)을 만들어줍니다.
        if str(k) == n:
            return i + 1
    return -1
