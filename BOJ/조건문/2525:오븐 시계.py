# 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.
# 현재 시간에서 입력 받은 시간만큼을 더해 주고 출력합니다. 60분이 되면 1시간이 오르는 것, 23시 다음은 0시인 것에 유의합니다.


# 내 풀이
H, M = map(int,input().split())
T = int(input())

M += T % 60   
H += T//60     # T를 받아 시와 분으로 나눠 각각에 더해준다.

if M >= 60:    #더한 결과 값으로 M 값이 60이 넘어가면  H에 1을 더해주고, M에 60을 뺀다.
    H += 1
    M -= 60
if H >= 24:    # 23시 59분에서 1분이 지나면 0시 0분이 되는 부분을 처리하기 위해 H가 24와 같거나 커지면 24를 빼준다.
    H -= 24
    
print(H,M)


# 다른사람 풀이

h,m=map(int,input().split())
t=h*60+m+int(input())
print(t//60%24,t%60)



 
