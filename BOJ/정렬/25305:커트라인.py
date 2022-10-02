# 첫째 줄에는 응시자의 수 N명과 상을 받는 사람의 수 k가 공백을 사이에 두고 주어지고, 둘째 줄에는 각 학생의 점수 $x$가 공백을 사이에 두고 주어진다.
# 점수들을 배열로 저장하고 내림차순으로 정렬하여 k-1번 째 값을 출력하면 커트라인이 출력됩니다.


# 내 풀이

import sys
input=sys.stdin.readline

n,k = map(int,input().split())       # 배열의 수 n과 커트라인 명 수 k를 입력
scores = list(map(int,input().split()))   # 점수 배열 scores를 입력

scores.sort(reverse=True)       # scores 배열을 내림차순으로 정렬
print(scores[k-1])        # 커트라인에 걸린 점수를 출력
