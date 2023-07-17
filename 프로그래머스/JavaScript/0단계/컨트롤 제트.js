// "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다. 
// 숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.

// 내 풀이
function solution(s) {
    let answer = [];
    let arr = s.split(' ')
    for(let a of arr){
        if (a === "Z"){
            answer.pop();
        }else{
            answer.push(Number(a))
        }
    }
    if (answer.length === 0){
        return 0
    }else{
    return answer.reduce((sum,curr) => sum+curr);
    }
}

// 개선한 내 풀이
function solution(s) {
    let answer = [];
    let arr = s.split(' ')
    for(let a of arr){
        if (a === "Z") answer.pop();
        else answer.push(Number(a))
    }
    return answer.length ? answer.reduce((sum,curr) => sum+curr) : 0;
}



// 다른사람 풀이1
function solution(s) {
    const stack = []

    s.split(' ').forEach((target) => {  // forEach 메서드는 다음 매개변수와 함께 배열의 각 요소에 적용하게 될 콜백 함수 전달
        if(target === 'Z') stack.pop();
        else stack.push(+target)
    })

    return stack.length ? stack.reduce((pre, cur) => pre + cur) : 0;
}


// 다른사람 풀이2
function solution(s) {

    let arr = s.split(" ");

    while ( arr.indexOf('Z') > -1) {

        arr.splice( arr.indexOf('Z')-1, 2);
    }

    return arr.reduce((a,b) => parseInt(a) + parseInt(b),0)
}
