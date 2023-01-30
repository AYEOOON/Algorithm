# 공은 1번부터 던지며 오른쪽으로 한 명을 건너뛰고 그다음 사람에게만 던질 수 있습니다. 
# 친구들의 번호가 들어있는 정수 배열 numbers와 정수 K가 주어질 때, k번째로 공을 던지는 사람의 번호는 무엇인지 return 하도록 solution 함수를 완성해보세요.
# 어려워서 못 푼 문제


# 풀이1 

def solution(numbers, k):
    players = numbers[0::2] if len(numbers) % 2 ==0 else numbers[0::2] + numbers[1::2]   # 만약 numbers의 길이가 짝수면 0부터 2칸씩 띄우고 홀수면 1부터 끝까지 리스트를 붙여서 구함
    return players[(k % len(players)) -1]           # k를 플래이어의 길이로 나눈 후 1을 뺀 값에 위치한 수를 리턴
  
  
# 풀이2

def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]
  
  
# 풀이3

def solution(numbers, k):
    return 2 * (k - 1) % numbers[-1] + 1
