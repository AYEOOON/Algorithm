# 약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 
# 자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.
# 풀지 못함


# 풀이1

def solution(n):
    num = []                  # 약수의 개수를 담을 리스트와 합성수 선언
    hapsung = 0
    
    for i in range(2, n+1):   # 2~n까지 약수의 개수를 구한다. 
        for j in range(1,i+1):
        
            if i%j == 0:      # 2~n까지 각 숫자에서 i%j == 0 즉 약수면 약수를 저장할 num에 저장한다.
                num.append(i) 
                
        if num.count(i) >= 3: # 약수를 담은 num에서 해당 i의 수를 count()함수를 이용하여 3이상 즉 합성수면 합성수의 카운트를 1증가한다.
            hapsung +=1
            
    return hapsung

# 풀이2

def solution(n):
    output = 0
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output
