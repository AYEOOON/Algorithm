# 필요한 저장 용량을 계산하는 프로그램을 작성해보자.

h, b, c, s = map(int,input().split())
print(round(h*b*c*s/8/1024/1024, 1), "MB")   # round 함수를 이용하여 소수1자리까지 표기
