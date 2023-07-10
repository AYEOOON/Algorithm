// my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.


// 내 풀이
function solution(my_string) {
    return my_string.split("").reverse().join("");
}

// 다른사람 풀이
// 스프레드 문법: https://learnjs.vlpt.us/useful/07-spread-and-rest.html
function solution(my_string) {
    var answer = [...my_string].reverse().join("");   // 스프레드 문법 사용
    return answer;
}
