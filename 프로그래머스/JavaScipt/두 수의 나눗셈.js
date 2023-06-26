/* 정수 num1과 num2가 매개변수로 주어질 때, num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 return 하도록 soltuion 함수를 완성해주세요.
answer에서 소수점 이하는 버림 */

// 내 풀이
function solution(num1, num2) {
    var answer = num1/num2*1000;
    return Math.floor(answer);
}


// 다른사람 풀이
function solution(num1, num2) {
    return Math.trunc(num1 / num2 * 1000);    // Math.trunc() 기능은 소수를 포함한 숫자에서 소수점은 삭제하고 정수부분만 반환을 하는 Math 객체의 메서드이다. 
}
