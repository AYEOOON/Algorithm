// 문자열 str1, str2가 매개변수로 주어집니다. str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.


// 내 풀이
function solution(str1, str2) {
    if (str1.includes(str2)) return 1
    else return 2
}

// 개선한 내 풀이
solution = (str1, str2) => (str1.includes(str2)) ? 1 : 2


// 다른사람 풀이1
function solution(str1, str2) {
    return str1.split(str2).length > 1 ? 1 : 2
}


// 다른사람 풀이2
function solution(str1, str2) {
    return str1.indexOf(str2) === -1 ? 2 : 1;
}
