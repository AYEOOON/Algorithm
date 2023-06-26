/*정수 num1과 num2가 매개변수로 주어집니다. 두 수가 같으면 1 다르면 -1을 retrun하도록 solution 함수를 완성해주세요.
삼항 연산자를 써서 풀어도 됨
삼항 연산자 = condition ? exprIfTrue : exprIfFalse*/


// 내 풀이
function solution(num1, num2) {
    if(num1 == num2){
        return 1
    }else{
        return -1
    }
}


// 다른사람 풀이
function solution(num1, num2) {
    var answer = num1 === num2 ? 1 : -1;
    return answer;
}

// 다른사람 풀이
const solution = (num1, num2) => num1 === num2 ? 1 : -1
