# a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다.
# 나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.


# 내 풀이

def solution(age):
    answer = ''
    word = ["a","b","c","d","e","f","g","h","i","j"]      # 알파벳을 word에 저장한다. 
    
    for i in str(age):              # age를 str형으로 변환하여 각 요소를 i에다가 넣음
        answer += word[int(i)]      # word에 str으로 바꿔준 age 를 인덱싱 하기 위하여 int()형으로 바꿔주고 각 인데스에 맞는 값을 answer에 저장한다.
        
    return answer
  
  
# 다른사람 풀이

def solution(age):

    return ''.join([chr(int(i)+97) for i in str(age)])
