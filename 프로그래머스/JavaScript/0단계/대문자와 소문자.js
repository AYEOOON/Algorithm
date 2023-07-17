// 내 풀이
function solution(my_string) {
    let answer = ''
    for(let a of my_string){
        if (a === a.toUpperCase()) answer += (a.toLowerCase())
        else answer += (a.toUpperCase())
    }
    return answer
}


// 다른사람 풀이1
function solution(my_string) {
    var answer = '';
    // for를 쓰면서 {}을 안쓸수 있다.
    for (let c of my_string) answer += c === c.toLowerCase() ? c.toUpperCase() : c.toLowerCase();
    return answer;
}


// 다른사람 풀이2(map 사용)
function solution(my_string) {
    return my_string.split('').map(n => n === n.toUpperCase() ? n.toLowerCase() : n.toUpperCase()).join('')
}
