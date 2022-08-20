# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
# 문자열을 입력받으면 문자열 중에서 가장 많이 사용된 알파벳을 출력하는 문제
# 입력받은 문자 중 중복되는 값을 제거한 리스트를 별수에 저장하고, 입력받은 문자열의 알파벳 개수를 세는데 이용


# 풀이
words = input().upper()                        # upper 함수를 이용하여 문자열을 모두 대문자로 변환
unique_words = list(set(words))                # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)                       # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :         # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])             # 숫자 리스트에서 가장 큰 수의 위치를 index 함수로 찾고, unique_words 리스트에서 같은 인덱스에 위치한 문자열을 출력
 
