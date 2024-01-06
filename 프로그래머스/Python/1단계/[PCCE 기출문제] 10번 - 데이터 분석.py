""" 
AI 엔지니어인 현식이는 데이터를 분석하는 작업을 진행하고 있습니다. 데이터는 ["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]으로 구성되어 있으며 현식이는 이 데이터들 중 조건을 만족하는 데이터만 뽑아서 정렬하려 합니다.

예를 들어 다음과 같이 데이터가 주어진다면

data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
주어진 데이터 중 "제조일이 20300501 이전인 물건들을 현재 수량이 적은 순서"로 정렬해야 한다면 조건에 맞게 가공된 데이터는 다음과 같습니다.
data = [[3,20300401,10,8],[1,20300104,100,80]]

정렬한 데이터들이 담긴 이차원 정수 리스트 data와 어떤 정보를 기준으로 데이터를 뽑아낼지를 의미하는 문자열 ext, 뽑아낼 정보의 기준값을 나타내는 정수 val_ext, 정보를 정렬할 기준이 되는 문자열 sort_by가 주어집니다.
data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후, sort_by에 해당하는 값을 기준으로 오름차순으로 정렬하여 return 하도록 solution 함수를 완성해 주세요. 단, 조건을 만족하는 데이터는 항상 한 개 이상 존재합니다.
"""

# 내 풀이
# 너무 복잡하게 푼 것같다. 
# 반복문에서 인덱스만 바꾸면 될 때 눈치채고 인덱스를 사용하면 좋을 것 같다.
def solution(data, ext, val_ext, sort_by):
    arr = []
    
    if ext == 'code':
        for i in range(len(data)):
            if data[i][0] < val_ext:
                arr.append(data[i])
                
    elif ext == 'date':
        for i in range(len(data)):
            if data[i][1] < val_ext:
                arr.append(data[i])
                
    elif ext == 'maximum':
        for i in range(len(data)):
            if data[i][2] < val_ext:
                arr.append(data[i])
                
    else:
        for i in range(len(data)):
            if data[i][3] < val_ext:
                arr.append(data[i])
                
    if sort_by == 'code':
        return sorted(arr, key = lambda x: x[0])
    elif sort_by == 'date':
        return sorted(arr, key = lambda x: x[1])
    elif sort_by == 'maximum':
        return sorted(arr, key = lambda x: x[2])
    elif sort_by == 'remain':
        return sorted(arr, key = lambda x: x[3])


# 다른사람풀이(인덱스를 잘 활용한 것같다.)
def solution(data, ext, val_ext, sort_by):
    answer = []
    by = [ "code", "date", "maximum", "remain" ]

    for item in data:
        if item[by.index(ext)] < val_ext:
            answer.append(item)

    return sorted(answer, key=lambda x: x[by.index(sort_by)])
