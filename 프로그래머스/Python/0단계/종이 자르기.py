# 머쓱이는 큰 종이를 1 x 1 크기로 자르려고 합니다. 예를 들어 2 x 2 크기의 종이를 1 x 1 크기로 자르려면 최소 가위질 세 번이 필요합니다.
# 정수 M, N이 매개변수로 주어질 때, M x N 크기의 종이를 최소로 가위질 해야하는 횟수를 return 하도록 solution 함수를 완성해보세요.
# 가로 세로의 길이가 정해진다. 그것들을 1의 길이로 나누려면 각 값의 -1만큼의 가위질이 필요하다.
# 종이를 자른다고 생각해서 반복문이라 생각해 어렵게 느껴졌던 것같다.
# 필기하면서 생각하면 단순하게 규칙찾는 문제인 것을 알 수 있었다. 



# 내 풀이

def solution(M, N):
    return M*N-1
  
  
# 다른사람 풀이

def get_cut_cnt_dfs(width, height):
    width, height = min(width, height), max(width, height)

    if width == 1 and height == 1:
        return 0

    return 1 + get_cut_cnt_dfs(width, height//2) + get_cut_cnt_dfs(width, height-height//2)

def solution(M, N):
    return get_cut_cnt_dfs(M, N)
