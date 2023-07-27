# 숫자나라 기사단의 각 기사에게는 1번부터 number까지 번호가 지정되어 있습니다. 기사들은 무기점에서 무기를 구매하려고 합니다.
# 각 기사는 자신의 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기를 구매하려 합니다. 
# 단, 이웃나라와의 협약에 의해 공격력의 제한수치를 정하고, 제한수치보다 큰 공격력을 가진 무기를 구매해야 하는 기사는 협약기관에서 정한 공격력을 가지는 무기를 구매해야 합니다.
# 무기를 만들 때, 무기의 공격력 1당 1kg의 철이 필요합니다. 그래서 무기점에서 무기를 모두 만들기 위해 필요한 철의 무게를 미리 계산하려 합니다.
# 기사단원의 수를 나타내는 정수 number와 이웃나라와 협약으로 정해진 공격력의 제한수치를 나타내는 정수 limit와 제한수치를 초과한 기사가 사용할 무기의 공격력을 나타내는 정수 power가 주어졌을 때, 무기점의 주인이 무기를 모두 만들기 위해 필요한 철의 무게를 return 하는 solution 함수를 완성하시오.


# 내 풀이
def solution(number, limit, power):
    weapon = [i for i in range(1, number+1)]
    arr = []
    for i in range(len(weapon)):
        a = 0
        for j in range(1, int(weapon[i]**(1/2)) + 1):
            if weapon[i]%j == 0:
                a += 1
                if j <weapon[i]//j:
                    a +=1
        arr.append(a)
    for k in range(len(arr)):
        if arr[k] > limit:
            arr[k] = power
    return sum(arr)



# 다른사람 풀이
def cf(n): # 공약수 출력
    a = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            a.append(n//i)
            a.append(i)
    return len(set(a))   # set함수로 중복되는 값을 제거하여 제곱수를 해결
def solution(number, limit, power):
    return sum([cf(i) if cf(i)<=limit else power for i in range(1,number+1)])
