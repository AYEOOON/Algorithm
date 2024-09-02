"""
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

- 구조대 : 119
- 박준영 : 97 674 223
- 지영석 : 11 9552 4421

전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.
"""

# 문자열을 정렬한다. (정렬하게 되면 자동으로 오름차순으로 정렬됨)
# 반복문을 돌려 이전 숫자가 현재 숫자의 앞쪽에 위치하면 False, 아니면 True 반환
# 문자열 중간에 이전 숫자가 있는 경우도 있기 때문에, 문자열을 이전 문자열 길이만큼 잘라서 비교해준다.


# 내 풀이
def solution(phone_book):
    phone_book.sort()

    for i in range(1, len(phone_book)):
        if phone_book[i-1] in (phone_book[i][:len(phone_book[i-1])]):
            return False
    return True
  

# 다른사람 풀이 1
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


# 다른사람 풀이 (해쉬)
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
