"""
채팅방에 누군가 들어오면 다음 메시지가 출력된다.

"[닉네임]님이 들어왔습니다."

채팅방에서 누군가 나가면 다음 메시지가 출력된다.

"[닉네임]님이 나갔습니다."

채팅방에서 닉네임을 변경하는 방법은 다음과 같이 두 가지이다.

1. 채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
2. 채팅방에서 닉네임을 변경한다.

채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record가 매개변수로 주어질 때,
모든 기록이 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return 하도록 solution 함수를 완성하라.
"""

"""
결국엔 최종적인 이름으로 입장과 퇴장을 기록하면 된다.
이중 for문을 사용하게 되면 시간 초과로 실패한다. 
"""

# 내 풀이
from collections import defaultdict

def solution(record):
    result = []
    user = {}
    
    for i in record:
        command = i.split()
        
        if command[0] == 'Enter':
            user[command[1]] = command[-1]
            
        elif command[0] == "Change":
            user[command[1]] = command[-1]
            
    for j in record:
        commands = j.split()
        
        if commands[0] == 'Enter':
            result.append(user[commands[1]] + '님이 들어왔습니다.')
            
          
        elif commands[0] == 'Leave':
            result.append(user[commands[1]] + '님이 나갔습니다.')
            
            
    return result

  
# 다른사람 풀이
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer
