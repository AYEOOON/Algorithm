# polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요.
# 같은 식이라면 가장 짧은 수식을 return 합니다.


# 내 풀이
def solution(polynomial):
    polynomial = polynomial.replace(' ','')
    arr1 = polynomial.split('+')
    a = []
    b = []
    for i in arr1:
        if 'x' in i:
            if i == 'x':
                a.append('1')
            else:
                a.append(i[0:len(i)-1])
        else: 
            b.append(i)
    a = sum(list(map(int,a)))
    b = sum(list(map(int,b)))
    if a == 0:
        return str(b)
    elif a == 1 and b == 0:
        return 'x'
    elif a == 1:
        return 'x'+' + '+str(b)
    elif b == 0:
        return str(a)+'x'
    else:
        return str(a)+'x'+' + '+str(b)


# 다른사람 풀이
def solution(polynomial):
    xnum = 0   # x계수
    const = 0  # 정수
    for c in polynomial.split(' + '): # +와 앞뒤 공백을 기준으로 문자열 분리
        if c.isdigit():  # 문자열도 isdigit()을 쓸 수 있다. 
            const+=int(c)  # c가 숫자면, const에 c더함
        else:
            xnum = xnum+1 if c=='x' else xnum+int(c[:-1])  # c가 x면 1을 더하고, 아니면 x를 제외한 부분까지 더함
    if xnum == 0:  # x의 계수가 0이면
        return str(const)
    elif xnum==1:  # x의 계수가 1이면
        return 'x + '+str(const) if const!=0 else 'x'  # 숫자부분이 0이 아니면 앞처럼 출력, 아니면 뒤처럼 출력
    else:
        return f'{xnum}x + {const}' if const!=0 else f'{xnum}x'
