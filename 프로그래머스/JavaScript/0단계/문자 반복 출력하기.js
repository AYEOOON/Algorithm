// my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.// 

// 내 풀이
function solution(my_string, n) {
    answer = [];
    for(let a of my_string) answer.push(a.repeat(n));
    return answer.join('');
}


// 다른사람 풀이1
function solution(my_string, n) {
    var answer = [...my_string].map(v => v.repeat(n)).join("");  //map을 사용해서 치환하는 방법
    console.log(answer);
    return answer;
}


// 다른사람 풀이2
function solution(my_string, n) {
    return my_string.split('').reduce((acc, cur) => acc + cur.repeat(n), '')
}
