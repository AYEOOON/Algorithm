# 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.
# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 
# 첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.


# 내 풀이

alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

time = 0
for unit in alpabet_list :  
    for i in unit:                                   # alpabet 리스트에서 각 요소를 꺼내서 한글자씩 분리
        for x in word :                              # 입력받은 문자를 하나씩 분리
            if i == x :                              # 두 알파벳이 같으면
                time += alpabet_list.index(unit) +3  # time = time + index +3
print(time)
