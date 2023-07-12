// 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.
// 오름차순만 생각하여 자바스크립트엔 -1이 마지막을 뜻하는것이 아니라는 것을 배열의 길이로 대체하였는데, 내림차순을 하면 간단한 것이였다. 


// 내 풀이
function solution(numbers) {
    numbers.sort((a,b)=> a-b);  // 오름차순 정렬
    return numbers[numbers.length-1]*numbers[numbers.length-2];  //배열길이의 마지막과 마지막 앞과 곱
}


// 다른사람 풀이
function solution(numbers) {
    numbers.sort((a,b)=>b-a);   // 내림차순
    return numbers[0]*numbers[1];  // 첫번째꺼와 두번째 수 곱
}


// 다른사람 풀이
function solution(numbers) {
    numbers = numbers.sort((a, b) => a - b);
    return numbers.at(-1) * numbers.at(-2);  // -1을 인덱스 마지막으로 표현하는 방법
}
