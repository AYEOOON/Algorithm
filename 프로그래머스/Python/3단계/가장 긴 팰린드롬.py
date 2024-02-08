"""
앞뒤를 뒤집어도 똑같은 문자열을 팰린드롬(palindrome)이라고 합니다.
문자열 s가 주어질 때, s의 부분문자열(Substring)중 가장 긴 팰린드롬의 길이를 return 하는 solution 함수를 완성해 주세요.
"""
"""
부분 문자열의 길이를 조절하면서 팰린드롬인지 검사 후 맞으면 끝에서 시작점을 뺀 길이 저장
"""

# 내 풀이
def solution(s):
    answer = 1
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            word = s[i:j]
            if word == word[::-1]:
                answer = max(answer, j-i)
    return answer
            
    # answer = 0
    # word1 = ''
    # for i in s:
    #     word1 += i
    #     if word1 == word1[::-1]:
    #         answer = max(len(word1), answer)
    # word2 = ''
    # for j in s[::-1]:
    #     word2 += j
    #     if word2 == word2[::-1]:
    #         answer = max(len(word2), answer)
    # return 1 if len(s) == 1 else answer
