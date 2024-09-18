"""
당신은 동영상 재생기를 만들고 있습니다. 당신의 동영상 재생기는 10초 전으로 이동, 10초 후로 이동, 오프닝 건너뛰기 3가지 기능을 지원합니다. 
각 기능이 수행하는 작업은 다음과 같습니다.

  - 10초 전으로 이동: 사용자가 "prev" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 전으로 이동합니다. 현재 위치가 10초 미만인 경우 영상의 처음 위치로 이동합니다. 영상의 처음 위치는 0분 0초입니다.
  - 10초 후로 이동: 사용자가 "next" 명령을 입력할 경우 동영상의 재생 위치를 현재 위치에서 10초 후로 이동합니다. 동영상의 남은 시간이 10초 미만일 경우 영상의 마지막 위치로 이동합니다. 영상의 마지막 위치는 동영상의 길이와 같습니다.
  - 오프닝 건너뛰기: 현재 재생 위치가 오프닝 구간(op_start ≤ 현재 재생 위치 ≤ op_end)인 경우 자동으로 오프닝이 끝나는 위치로 이동합니다.
  
동영상의 길이를 나타내는 문자열 video_len, 기능이 수행되기 직전의 재생위치를 나타내는 문자열 pos, 오프닝 시작 시각을 나타내는 문자열 op_start, 오프닝이 끝나는 시각을 나타내는 문자열 op_end, 사용자의 입력을 나타내는 1차원 문자열 배열 commands가 매개변수로 주어집니다. 
이때 사용자의 입력이 모두 끝난 후 동영상의 위치를 "mm:ss" 형식으로 return 하도록 solution 함수를 완성해 주세요.
"""

# 내 풀이
def solution(video_len, pos, op_start, op_end, commands):

    # 시간 형식 변경 
    end = int(video_len.split(":")[0])*60+int(video_len.split(":")[1])
    op_start= int(op_start.split(":")[0])*60+int(op_start.split(":")[1])
    op_end = int(op_end.split(":")[0])*60+int(op_end.split(":")[1])
    now = int(pos.split(":")[0])*60+int(pos.split(":")[1])
    
    for com in commands :
        if now >= op_start and now <= op_end:
            now = op_end
        
        if com == "next":
            now = min(now + 10, end)
            
        if com == "prev":
            now = max(now - 10, 0)
            
        if now >= op_start and now <= op_end:
            now = op_end  

    s = str(now%60).zfill(2) # 두자리가 되게 0 채우기
    m = str(now // 60).zfill(2)
    
    return "{0}:{1}".format(m, s)


# GPT 풀이
def time_to_seconds(time_str):
    minutes, seconds = map(int, time_str.split(":"))
    return minutes * 60 + seconds

def seconds_to_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return "{:02}:{:02}".format(minutes, seconds)

def solution(video_len, pos, op_start, op_end, commands):
    video_len = time_to_seconds(video_len)
    pos = time_to_seconds(pos)
    op_start = time_to_seconds(op_start)
    op_end = time_to_seconds(op_end)
    
    for command in commands:
        # 오프닝 구간 체크
        if op_start <= pos <= op_end:
            pos = op_end

        # 명령어 처리
        if command == "next":
            pos = min(pos + 10, video_len)
        elif command == "prev":
            pos = max(pos - 10, 0)

        # 오프닝 구간 체크
        if op_start <= pos <= op_end:
            pos = op_end

    return seconds_to_time(pos)
