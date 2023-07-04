# 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.
# 너무 어렵게 생각한 문제..
# 수와 박을 따로 보는것이 아니라 수박을 하나로 봐야 풀리는 문제

# 내 풀이
def solution(n):
    word = '수박'
    return word*(n//2)+word[:n%2]

# 다른사람 풀이1(효율은 좋지 않지만 창의적인 풀이)
def water_melon(n):
    str = "수박"*n
    return str[:n]

# 다른사람 풀이2
def solution(n):
    return "".join(["수박"[i%2] for i in range(n)])
