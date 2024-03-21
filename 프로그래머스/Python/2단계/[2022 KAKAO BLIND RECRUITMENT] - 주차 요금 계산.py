"""
주차장의 요금표와 차량이 들어오고(입차) 나간(출차) 기록이 주어졌을 때, 차량별로 주차 요금을 계산하려고 합니다. 

- 어떤 차량이 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주합니다.
- 00:00부터 23:59까지의 입/출차 내역을 바탕으로 차량별 누적 주차 시간을 계산하여 요금을 일괄로 정산합니다.
- 누적 주차 시간이 기본 시간이하라면, 기본 요금을 청구합니다.
- 누적 주차 시간이 기본 시간을 초과하면, 기본 요금에 더해서, 초과한 시간에 대해서 단위 시간 마다 단위 요금을 청구합니다.
    -초과한 시간이 단위 시간으로 나누어 떨어지지 않으면, 올림합니다.
    -⌈a⌉ : a보다 작지 않은 최소의 정수를 의미합니다. 즉, 올림을 의미합니다.

주차 요금을 나타내는 정수 배열 fees, 자동차의 입/출차 내역을 나타내는 문자열 배열 records가 매개변수로 주어집니다. 
차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return 하도록 solution 함수를 완성해주세요.
"""

# 내 풀이
from datetime import datetime
import math

def solution(fees, records):
    result = []  # 정답을 담는 배열
    state = {}   # 차량의 입차 시간을 담는 딕셔너리
    car_dict = {} # 차량의 누적 주차시간을 담는 딕셔너리
    
    for i in records:
        time, num, re = i.split()  # 시간, 차량 번호, 상태 저장
        if num not in car_dict:  # 만약에 누적 주차시간에 차량이 등록되지 않았다면 
            car_dict[num] = 0  # 차량 추가 후 초기화 
        if re == 'IN': # 입차
            state[num] = time  # 입차 시간 등록
        elif re == 'OUT':  # 출차
            in_time = datetime.strptime(state[num], "%H:%M")  # 들어온 시간
            out_time = datetime.strptime(time, "%H:%M")   # 나간 시간
            p_time = ((out_time - in_time).seconds)//60  # 시간차를 초로 변환한 후, 분으로 바꿈
            car_dict[num] += int(p_time) # 누적시간 저장
            state.pop(num, None)  # 차량 출차 처리

    for i in state:  # 출차하지 않은 차들
        in_time = datetime.strptime(state[i], "%H:%M")
        last_time = datetime.strptime('23:59', "%H:%M")  # 마지막 시간을 23:59로 처리
        p_time = ((last_time - in_time).seconds)//60
        car_dict[i] += int(p_time)
        
    for k in sorted(car_dict):  # 차량 오름차순 정렬
        fee = fees[1]  # 기본 요금 저장
        if car_dict[k] <= fees[0]:  # 기본 시간 이하라면
            result.append(fee)  # 그대로 저장
        else:  # 기본시간 이상이라면
            fee += math.ceil((car_dict[k] - fees[0])/fees[2]) * fees[3]  # 요금 계산
            result.append(fee) # 저장
            
    return result



# 다른사람 풀이
from collections import defaultdict
from math import ceil

class Parking:
    def __init__(self, fees):
        self.fees = fees
        self.in_flag = False
        self.in_time = 0
        self.total = 0

    def update(self, t, inout):
        self.in_flag = True if inout=='IN' else False
        if self.in_flag:  self.in_time = str2int(t)
        else:             self.total  += (str2int(t)-self.in_time)

    def calc_fee(self):
        if self.in_flag: self.update('23:59', 'out')
        add_t = self.total - self.fees[0]
        return self.fees[1] + ceil(add_t/self.fees[2]) * self.fees[3] if add_t >= 0 else self.fees[1]

def str2int(string):
    return int(string[:2])*60 + int(string[3:])

def solution(fees, records):
    recordsDict = defaultdict(lambda:Parking(fees))
    for rcd in records:
        t, car, inout = rcd.split()
        recordsDict[car].update(t, inout)
    return [v.calc_fee() for k, v in sorted(recordsDict.items())]
