// 두 배열이 얼마나 유사한지 확인해보려고 합니다. 
// 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.


// 내 풀이
function solution(s1, s2) {
    var answer = 0;
    for(let a of s1){
        for(let b of s2){
            if(a===b) answer += 1;
        }
    }
    return answer;
}


//  다른사람 풀이1
function solution(s1, s2) {
  return s1.filter((v) => s2.includes(v)).length;
}

// 다른사람 풀이2
function solution(s1, s2) {
    let count = 0;
    for (let v of s1) if (s2.includes(v)) count++;  // for문을 한번만씀
    return count;
}
