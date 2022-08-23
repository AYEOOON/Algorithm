# 랜덤으로 숫자를 입력받은 뒤 1부터 입력받은 숫자까지의 범위 안에서 숫자의 각 자리 숫자가 등차수열을 이루는 수가 몇 개인지를 출력하는 문제이다.
# 등차수열인지 비교대상이 없기 때문에 모두 한수이고 세자리 숫자는 각 자리의 숫자 간격이 동일하면 한수이다.
# 세자리 숫자에서 각자리 숫자 간격을 어떻게 비교할지 고민함



# 내 풀이

def hansu(num) :
    hansu_cnt = 0
    for i in range(1, num+1):
        num_list = list(map(int,str(i)))     # for문의 변수 i를 str함수로 문자열로 변환시키고서 각 자릿수를 분리해서 다시 int 타입으로 변환시켰다. 
        if i < 100:
            hansu_cnt += 1                            # 100보다 작으면 모두 한수
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:   # 앞의 두 자리의 차이와 뒤의 두 자리의 차이가 같으면 한수이다.
            hansu_cnt += 1                            # x의 각 자리가 등차수열이면 한수
    return hansu_cnt

num = int(input())
print(hansu(num))
 
 

# 다른사람 풀이

print(sum(i<100 or i//10%10*2==i%10+i//100 for i in range(1,int(input())+1)))
