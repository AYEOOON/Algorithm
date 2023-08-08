// 정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
// 만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.


// 내 풀이
function solution(l, r) {
    let answer = []
    for(let i = l; i <= r; i++){
        if (/^[05]+$/.test(i)){
            answer.push(i)
        }
    }
    return answer.length? answer : [-1];
}


// 다른사람 풀이
function solution(l, r) {
    const result = Array.from({length:r-l+1}, (_,i)=>i+l).filter(n=>!/[^05]/.test(n));
    return result.length ? result : [-1];
}
