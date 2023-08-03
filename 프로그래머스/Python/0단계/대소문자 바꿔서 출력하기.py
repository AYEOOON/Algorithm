# 영어 알파벳으로 이루어진 문자열 str이 주어집니다.
# 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

# 내 풀이
str = input()
arr =  []
for i in str:
    if i.isupper():
        arr.append(i.lower())
    else:
        arr.append(i.upper())
print(''.join(arr))

# 개선한 내 풀이
print(''.join(x.upper() if x == x.lower() else x.lower() for x in input()))


# 다른사람 풀이
print(input().swapcase())  # swapcase(): 대소문자를 전환하는 함수
