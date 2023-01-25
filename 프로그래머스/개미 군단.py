# 각각의 공격력이 장군개미는 5, 병정개미는 3, 일개미는 1이다. 
# 사냥꾼의 hp가 주어졌을 때 딱 맞게 최소한의 병력을 구성하려면 몇 마리의 개미가 필요한지를 return하도록 solution 함수를 완성해주세요.


# 내 풀이

def solution(hp):
    gen = hp//5
    sol = (hp-(5*gen))//3
    work = ((hp-(5*gen))-(3*sol))//1
    
    return gen+sol+work

# 다른사람 풀이

def solution(hp):    
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)
