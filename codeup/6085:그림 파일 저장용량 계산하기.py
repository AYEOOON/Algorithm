# 이미지의 가로 해상도 w, 세로 해상도 h, 한 픽셀을 저장하기 위한 비트 b 가 주어질 때, 압축하지 않고 저장하기 위해 필요한 저장 용량을 계산하는 프로그램을 작성해 보자.



w, h, b = map(int, input().split())
m = (w*h*b)/(8*1024*1024)
print(format(m,".2f"), "MB") # format : 0으로 나누어 떨어져도 2번째 자리까지 0으로 채워줌.
                             # round : 0으로 나누어 떨어져도 첫번째 자리까지만 0으로 채워줌 
