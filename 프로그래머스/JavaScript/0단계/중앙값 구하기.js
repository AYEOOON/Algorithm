/* 정수 배열 array가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요.
   처음엔 sort()만 이용해서 풀었는데, 계속 실패해서 찾아보니 sort()만 쓰면 "90"과 "100"을 비교 시 앞자리 9와 1을 비교, 100보다 90이 더 크다는 결론을 내린다.
   따라서 이런 이유로 숫자를 비교하기 위해선 별도로 정의된 compare function을 이용해야하는 것이다.
*/

// 내풀이
function solution(array) {
    array.sort(function(a,b) {return a-b});
    return array[Math.trunc(array.length/2)]
}

// 다른사람 풀이
function solution(array) {
  return array.sort((a, b) => a - b)[Math.floor(array.length / 2)];  //외워놓는것이 좋겠다. 
}
