// 정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다. 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.
// unshift안에 배열인덱스를 넣으면 null이 채워져 실패하였는데, numbers.pop()을 넣으니 해결되었다. 


// 내 풀이
function solution(numbers, direction) {
    if(direction === "right"){
        numbers.unshift(numbers.pop());
    }else{
        numbers.push(numbers.shift());
    }
    return numbers
}


// 다른사람 풀이
function solution(numbers, direction) {
    direction === 'right' ? numbers.unshift(numbers.pop()) : numbers.push(numbers.shift());
    return numbers;
}

