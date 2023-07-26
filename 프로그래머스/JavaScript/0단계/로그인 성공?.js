// 내 풀이
function solution(id_pw, db) {
    let [login_id, login_pw] = id_pw
    const answer =[]
    for(let a of db){
        let [id, pw] = a;
        if (login_id === id){
            if(login_pw === pw) return "login"
            else if (login_pw != pw) return "wrong pw"
        }
    }
    return "fail"
}

// 개선한 내 풀이
function solution(id_pw, db) {
    let [login_id, login_pw] = id_pw
    for(let [id, pw] of db){
        if (login_id === id)
            if(login_pw === pw) return "login"
            else if (login_pw != pw) return "wrong pw"
    }
    return "fail"
}


// 다른사람 풀이1
function solution(id_pw, db) {
  const [id, pw] = id_pw;
  const map = new Map(db);  // db의 키, 값 쌍으로 저장
  // 만약 map에 id가 없으면 "fail" =, 있으면 id값에 맞는 pw값 반환, 만약 같다면 "login", 아니면 "wrong pw"
  return map.has(id) ? (map.get(id) === pw ? 'login' : 'wrong pw') : 'fail';
}


// 다른사람 풀이2
unction solution(id_pw, db) {
    db = db.filter(v=>v[0]===id_pw[0]);  // id가 서로 같은 것만 배열에 저장
 
    if (!db.length) return 'fail';  // 아무것도 없으면 "fail"

    for (let d of db) if (d[1] === id_pw[1]) return 'login';  // pw가 서로 같으면 "login" 

    return 'wrong pw';
}
