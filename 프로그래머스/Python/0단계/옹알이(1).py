# 머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다.
# 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 
# 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.


# 풀이1(isdigit()함수 사용)

def solution(babbling):
    answer = 0
    count = 0
    bab_r = []
    for bab in babbling:
        bab = bab.replace('aya','1')
        bab = bab.replace('ye','2')
        bab = bab.replace('woo','3')
        bab = bab.replace('ma','4')
        if bab.isdigit() == True:
            count += 1


    return count
  
  
# 풀이2

def solution(babbling):
    answer = 0
    prono = ['aya','ye','woo','ma']
    for i in babbling :
        for j in prono :
            if j+j in i :
                break
            else :
                i = i.replace(j,"").strip()
        if i :
            continue
        else :
            answer += 1
    return answer
    
    
 # 풀이3 ( lamda 사용)
 
 def solution(babbling):
    return len(list(filter(lambda x: x.replace("aya", "").replace("ye", "").replace("woo", "").replace("ma", "") == "" and "ayaaya" not in x and "yeye" not in x and "woowoo" not in x and "mama" not in x, babbling)))
