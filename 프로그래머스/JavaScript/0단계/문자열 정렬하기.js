//문자열 my_string이 매개변수로 주어질 때, my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.


// 내 풀이
// 정규식으로 숫자만 분리한 뒤 숫자로 변경 후 배열로 만들고, 오름차순으로 변경
function solution(my_string) {
    return Array.from(my_string.replace(/[^0-9]/g,''),(arg) => Number(arg)).sort((a,b) => a-b);
}


// 다른사람 풀이
function solution(my_string) {
    return my_string.match(/\d/g).sort((a, b) => a - b).map(n => Number(n));
}
