// 문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.
// 자바스크립트에는 isUpper이 없기때문에 대문자와 비교를 하여 구분해야한다. 
// 자바스크립트에는 toUpperCase(), toLowerCase() 로 대소문자 전환한다.

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
