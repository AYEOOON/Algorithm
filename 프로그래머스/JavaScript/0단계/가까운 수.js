// 정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.

// 내 풀이
function solution(array, n) {
    array.sort((a,b) => a-b);
    const arr = array.map(x => Math.abs(x-n));
    return array[arr.indexOf(Math.min(...arr))]
}

// 다른사람 풀이
const solution = (array, n) => {
    array.sort((a,b) => Math.abs(n - a) - Math.abs(n - b) || a - b);
    return array[0];
}
