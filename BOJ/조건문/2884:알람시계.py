# 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것이다.
# 입력받는 시간은 24시간 개념으로 입력받는다.


# 내 풀이
H, M = map(int,input().split())

if M < 45 :	     # 분단위가 45분보다 작을 때 
    if H == 0 :	 # 0 시이면
        H = 23
        M += 60
    else :	     # 0시가 아니면 (0시보다 크면)
        H -= 1	
        M += 60
        
print(H, M-45)


# 다른사람 풀이

a,b=map(int,input().split());x=a*60+b-45;print(x//60%24,x%60)


# 9월 13일 

H, M = map(int,input().split())

if M >= 45:
  print(H,M-45)
  
elif M < 45:
  if H < 1:
    print((H+24)-1, (M-60)-45)   # 24시 시간 표현을 사용해야하므로 입력받은 시간에 24를 더한 뒤 분으로 넘겨 1시간을 뺴준다.

  else:
    print((H-1),(M+60)-45)
    
