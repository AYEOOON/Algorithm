# 셀프 넘버는 양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다.
# 예를 들어, 33으로 시작한다면 다음 수는 33 + 3 + 3 = 39이고, 그 다음 수는 39 + 3 + 9 = 51, 다음 수는 51 + 5 + 1 = 57이다.
# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.



# 풀이

def self_Number(n):                 # 백준문제에 나온 d(n) 함수 
    number = n # 33이 들어오면
    for i in list(str(n)):          # 리스트로 쪼개서 [3,3] 으로 나누고
        number += int(i)            # 즉 33 + 3 + 3
    return number                   #그대로 리턴

arr = []                            #셀프넘버 아닌애들을 담을 배열

for i in range(10000):              #10000까지 돌림
    arr.append(self_Number(i))      #셀프넘버 아닌 수을 넣어줌

for j in range(10000):              #마찬가지로
    if j in arr:                    # j에 arr랑 일치하는게 있으면 
        pass                        #그냥 pass pass는 말그대로 넘어가라는거임
    else:
        print(j)                    #없으면 셀프넘버라는거니까 출력
        
        
        
# 다른 풀이

numbers = list(range(1,10_001))     # 10_001이라고 중간에 언더바를 넣어 큰수의 구분을 쉽게할 수 있음
remove_list=[]                      # 생성자 리스트(나중에 삭제)
for num in numbers:
    for n in str(num):              # str으로 저장하는 이유는 각 자리수 분산은 int형에서는 불가능하고, str형에서만 가능
        num += int(n)               # num = num + int(n)
    if num <= 10_000:             
        remove_list.append(num)     # 생성자가 10000보다 작으면 append함수를 사용해 remove_list에 올림
for remove_num in set(remove_list): # remove_list에는 중복된 숫자가 많아 set 함수를 이용해 중복된 숫자를 정리
    numbers.remove(remove_num)      # 위에 것을 범위로 하는 remove_num을 만듦
for self_num in numbers:            # 맨 처음 생성했던 리스트 numbers에는 remove_num을 제거
    print(self_num)                 # numbers를 범위로 최종 구하는 값인 self_num을 지칭해주고 출력
