# 연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 두 정수 num과 total이 주어집니다. 연속된 수 num개를 더한 값이 total이 될 때, 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.


# 내 풀이(보잘거없는)
def solution(num, total):
    answer = []
    if num%2 == 0:
        for j in range(0,num//2):
            answer.append(total//num-j)
        for i in range(1,num//2+1):
            answer.append(total//num+i)
    else:
        for i in range(1,num//2+1):
            answer.append(total//num-i)
        for j in range(0,num//2+1):
            answer.append(total//num+j)
            
    if(num == 0):
        result.append(0)
        
    return sorted(answer)

# 개선한 풀이(내가 한건아니고)
def solution(num, total):
    answer = []
    middle = total//num
    
    if num%2 == 1:
        for i in range(middle-num//2, middle+num//2+1):
            answer.append(i)
    else:
        for i in range(middle-num//2+1, middle+num//2+1):
            answer.append(i)
            
    return answer


# 다른사람 풀이1
def solution(num, total):
    return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]


# 다른사람 풀이2
def solution(num, total):
    answer = []
    var = sum(range(num+1))
    diff = total - var
    start_num = diff//num
    answer = [i+1+start_num for i in range(num)]
    return answer


# 다른사람 풀이3
def solution(num, total):
    if num % 2 == 1:
        return list(range(total//num-num//2, total//num+num//2+1))
    else:
        return list(range(total//num-num//2+1, total//num+num//2+1))
