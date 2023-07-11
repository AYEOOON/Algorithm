// 정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.
// 계속 1,2,3이 나와서 원인을 몰랐는데 slic()로 배열을 복사하여 해결하였다. 

// 내 풀이
function solution(emergency) {
    let arr = emergency.slice().sort((a,b) => b-a);  // slice()를 이용하여 배열을 복사
    return emergency.map(t => arr.indexOf(t)+1);  
}
