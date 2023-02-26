# 머쓱이가 입력한 아이디와 패스워드가 담긴 배열 id_pw와 회원들의 정보가 담긴 2차원 배열 db가 주어질 때, 다음과 같이 로그인 성공, 실패에 따른 메시지를 return하도록 solution 함수를 완성해주세요.
# 아이디와 비밀번호가 모두 일치하는 회원정보가 있으면 "login"을 return합니다.
# 로그인이 실패했을 때 아이디가 일치하는 회원이 없다면 “fail”를, 아이디는 일치하지만 비밀번호가 일치하는 회원이 없다면 “wrong pw”를 return 합니다.
# 접근은 비슷했지만 풀지 못함


# 풀이1

def solution(id_pw, db):
    login_id, login_pw = id_pw   # 리스트에 갯수에 맞게 변수에 할당할 수 있는 것이 중요
    for db_login in db:
        db_id,db_pw = db_login
        
        if login_id == db_id:
            if login_pw == db_pw:
                return "login"
            if login_pw != db_pw:
                return "wrong pw"
        
    return "fail"
  
# 풀이2
# :=는 Python 3.8에서 새로 나온 기능.
# :=는 대입 표현식이지만, 바다 코끼리 연산자라고도 불린다. 표현식에 이름을 부여하고 재사용할 수 있게 하는 것


def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):     # dict(db) 형변환: 리스트의 값들이 key/value 쌍을 맞출 수 있는 2개로 구성되어 있으면, dictionary 형태로 변경이 가능.
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"
