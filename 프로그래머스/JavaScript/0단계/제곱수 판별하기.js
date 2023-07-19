// 어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.

// 내 풀이
solution = n => (Math.trunc(n**0.5)**2 === n) ? 1 : 2


// 다른사람 풀이
function solution(n) {
  // n의 제곱근이 정수면(isInteger) 1, 아니면 2
  return Number.isInteger(Math.sqrt(n)) ? 1 : 2;  // pow: 제곱, sqrt: 제곱근
}
