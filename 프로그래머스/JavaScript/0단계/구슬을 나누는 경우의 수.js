// 머쓱이가 갖고 있는 구슬의 개수 balls와 친구들에게 나누어 줄 구슬 개수 share이 매개변수로 주어질 때, balls개의 구슬 중 share개의 구슬을 고르는 가능한 모든 경우의 수를 return 하는 solution 함수를 완성해주세요.
// 조합 문제
// 조합 = n!/((n-m)!*m!)
// 재귀를 사용하여 풀었다.

// 내 풀이
function solution(balls, share) {
    return factorial(balls)/ (factorial((balls-share))*factorial(share));
}

function factorial(num){
  let returnFactorial = BigInt(1);   // BigInt형식을 사용해야 balls, share의 범위를 감당
    for(let i = num; i>=2; i--){
        returnFactorial*=BigInt(i)
    }
    return returnFactorial;
}


// 다른사람 풀이1
const 팩토리얼 = (num) => num === 0 ? 1 : num * 팩토리얼(num - 1)

function solution(balls, share) {
  return Math.round(팩토리얼(balls) / 팩토리얼(balls - share) / 팩토리얼(share))
}


// 다른사람 풀이2
function solution(balls, share) {
    var result = 1;
    while(share > 0){
        result = result * balls / share;
        balls = balls - 1;
        share = share - 1;
    }
    return Math.round(result);
}
