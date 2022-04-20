# 월이 입력될 때 계절 이름이 출력되도록 해보자


# 내 풀이

n = int(input())

if n <= 5 and 2<n:
  print("spring")
  
elif n <= 8 and 5<n :
  print("summer")
  
elif n <= 11 and 8<n :
  print("fall")
  
elif n <=2 or n == 12:
  print("winter")
  
  
# 다른 사람의 풀이

a = int(input())


if a//3 ==1 :
print("spring")

elif a//3 == 2 :
print("summer")

elif a//3 == 3:
print("fall")

else :
print("winter")


