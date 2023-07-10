// my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.


// 내 풀이
function solution(my_string, letter) {
    return my_string.replaceAll(letter, '');
}


// 다른사람 풀이
function solution(my_string, letter) {
    const answer = my_string.split(letter).join('')  //split의 인자를 기준으로 분리 -> 배열로 반환
    return answer;
}
