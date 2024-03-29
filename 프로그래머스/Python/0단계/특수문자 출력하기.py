# !@#$%^&*(\'"<>?:;를 그대로 출력하는 문제

# 내 풀이
print('!@#$%^&*(\\\'\"<>?:;')

# \": 쌍따옴표
# \\: 백슬래시
# r'문자열': 이스케이프 문자의 의미 무시, 그대로 출력

# 다른사람 풀이
print(r'!@#$%^&*(\'"<>?:;')  # raw 를 의미하는 r로, regex 에서 pattern 설정 시 escape 문자를 많이 써야해서 자주 사용
