# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.


# 내 풀이

year = int(input())

if (year%4 == 0 and (year%100 != 0 or year%400 == 0)) :     # year이 4의 배수이고 100의 배수가 아니거나 또는 400의 배수일 때 if문
    print('1')
else:
    print('0')
    
    
# 삼항 연산자로 푼 다른 풀이

year = int(input())

print('1') if ((year%4 == 0)and(year%100 != 0)) or (year%400 == 0) else print('0')


# 다른사람 풀이

a=int(input())

if a%4==0 and a%100!=0 or a%400==0:
    print(1)
else:
    print(0)
