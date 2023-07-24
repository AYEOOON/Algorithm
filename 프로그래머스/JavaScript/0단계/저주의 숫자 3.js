// 정수 n이 매개변수로 주어질 때, n을 3x 마을에서 사용하는 숫자로 바꿔 return하도록 solution 함수를 완성해주세요.
// 3의 배수와 숫자 3을 배열에서 뺀 뒤 인덱스를 찾으면 된다. 


// 내 풀이
function solution(n) {
    const arr = Array(230).fill(1).map((n, idx) => n + idx)
    return arr.filter(el => el%3!=0 && el%10!=3 && (el<30 || el>=40) && (el<130 || el >= 140))[n-1]
}


// 다른사람 풀이
function solution(n) {
  return [...Array(n * 3)]
    .map((_, i) => i + 1)
    .filter((num) => num % 3 !== 0 && !num.toString().includes("3"))[n - 1];
}
