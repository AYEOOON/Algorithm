# 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다.
# 선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때, 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.
# 기존의 swap하는 방식은 런타임에러를 발생 시킨다. 
# 따라서 딕셔너리를 사용하여 해결하였다.


# 내 풀이
def solution(players, callings):
    dic = {player:i for i,player in enumerate(players)}  # 선수:등수
    
    for i in callings:
        index = dic[i]  # 호명된 선수의 현재 등수
        
        players[index], players[index-1] = players[index-1],players[index] # 위치 변경
        
        dic[players[index]] = index  # 앞사람에게 호명된 선수의 등수를 할당
        dic[players[index-1]] = index-1  # 호명된 선수의 등수-1
        
    return sorted(dic,key = lambda x: dic[x])


# 다른사람 풀이
def solution(players, callings):
    result = {player: i for i, player in enumerate(players)} # 선수: 등수
    for who in callings:
        idx = result[who] # 호명된 선수의 현재 등수
        result[who] -= 1 # 하나 앞 등수로 바꿔줌 -1
        result[players[idx-1]] += 1 # 앞에 위치했던 선수의 등수 +1
        players[idx-1], players[idx] = players[idx], players[idx-1] # 위치 변경
    return players
