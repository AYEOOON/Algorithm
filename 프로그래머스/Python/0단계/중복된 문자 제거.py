# 문자열 my_string이 매개변수로 주어집니다.
# my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.
# 참고: https://11001.tistory.com/81


# 내 풀이

def solution(my_string):
    return ''.join(dict.fromkeys(my_string))    # https://velog.io/@jaylnne/python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-dict.fromkeys-%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC-%EC%83%9D%EC%84%B1-%EB%A9%94%EC%86%8C%EB%93%9C-%EC%A0%95%EB%A6%AC
