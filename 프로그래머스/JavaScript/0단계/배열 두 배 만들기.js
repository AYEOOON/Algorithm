// 정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.


// 내 풀이
function solution(numbers) {
    var answer = [];
    for(let i = 0; i < numbers.length; i ++){
     answer.push(numbers[i]*2)   
    }
    return answer;
}

// 다른사람 풀이(reduce 사용법)
function solution(numbers) {
    return numbers.reduce((a, b) => [...a, b * 2], []);
}

// 다른사람 풀이(map 사용법)
const solution = (numbers) => numbers.map((number) => number * 2)
