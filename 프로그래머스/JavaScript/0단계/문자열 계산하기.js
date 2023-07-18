// my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.

// 내 풀이
function solution(my_string) {
    return eval(my_string);
}


// 다른사람 풀이1
function solution(my_string) {
    const stack = [];

    let sign = 1;
    for (const ch of my_string.split(" ")) {
        if (ch === "+") {
            sign = 1;
        } else if (ch === "-") {
            sign = -1;
        } else {
            stack.push(ch * sign);
        }
    }

    return stack.reduce((a,b) => a + b, 0);
}


// 다른사람 풀이2
// 1. arr.unshift => 배열의 맨 앞에 넣어준다.
// 2. +arr.shift() => 배열의 맨 앞에서 뺀 것을 integer
// 3. (arr.shift() === "+" ? 1 : -1) * arr.shift()) => 배열의 맨 앞에서 다시 뺀 것이 +면 1을, -면 -1을 다시 배열의 맨 앞에서 뺀 것에 곱해준다. 
function solution(my_string) {
    const arr = my_string.split(' ').filter(e=>e);
    while(arr.length > 1) arr.unshift(+arr.shift() + (arr.shift() === "+" ? 1 : -1) * arr.shift())  
    return arr[0]
}
