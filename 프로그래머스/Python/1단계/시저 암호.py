# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.
# "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 


# 내 풀이
def solution(s, n):
    answer = []
    lowword = 'abcdefghijklmnopqrstuvwxyz'
    upword = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in s:
        if i == " ":
            answer.append(" ")
        elif i.isupper():
            answer.append(upword[(upword.index(i)+n)%26])
        else:
            answer.append(lowword[(lowword.index(i)+n)%26])
    return ''.join(answer)


# 다른사람 풀이1
# ord(문자) : 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환.(ord('a')를 넣으면 정수 97을 반환)
# chr(정수) : 하나의 정수를 인자로 받고 해당 정수에 해당하는 유니코드 문자를 반환(하나의 정수를 인자로 받고 해당 정수에 해당하는 유니코드 문자를 반환)
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))  # 값을 더해줌으로써 chr로 형변환 했을 때 알파벳이 저장
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)



# 다른사람 풀이2
def solution(s, n):
    answer = ''
    for i in s:
        if i:
            if i >= 'A' and i <= 'Z':  # 문자열도 부등호 가능
                answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
            elif i >= 'a' and i <= 'z':
                answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
            else : answer += ' '
    return answer
