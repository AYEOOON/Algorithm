# 두 정수 A와B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.


While True:  #  While문을 True로 두어 계속 반복하게 함
    A, B = map(int,input().spilt())
    if ((A == 0) and (B == 0)):
        break
    else:
        print(A+B)
