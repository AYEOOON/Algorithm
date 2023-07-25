// 정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다. 
// 이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 정수가 담긴 배열 numlist와 정수 n이 주어질 때 numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.


// 내 풀이
function solution(numlist, n) {
    return numlist.sort((a,b)=>{
        const [agap, bgap] = [Math.abs(a-n), Math.abs(b-n)]
        
        if (agap === bgap) return b-a
        
        return agap-bgap  // 절대값 차이를 기준으로 오름차순 정렬
    })
}



// 다른사람 풀이
// sort함수를 보면 음수를 반환하면 a가 먼저, 양수면 b가 순서가 먼저 되도록 짜여져 있고
// b랑 a의 거리가 같은 상황 즉 Math.abs(a - n) - Math.abs(b - n)이게 0이 되는 상황이 되면 ||연산자 뒤가 실행되면서 같은 거리일 경우 큰 수를 먼저 나오도록 함
function solution(numlist, n) {
  return numlist.sort((a, b) => Math.abs(a - n) - Math.abs(b - n) || b - a);
}
