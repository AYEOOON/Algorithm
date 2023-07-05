// n이 주워지면, n이하의 수 중 홀수만 저장한 배열을 출력하는 문제

// 내 풀이
function solution(n) {
    var arr = [];
    for(i=1;i <= n;i++){    //n이 중요하다..
        if (i%2===1){
            arr.push(i);
        }
    }
    return arr;
}


// 다른사람 풀이1
function solution(n) {
    var answer = [];

    for (let i = 1; i<=n; i+=2) answer.push(i)   // i+=2..

    return answer;
}

// 다른사람 풀이2(인덱스 활용)
function solution(n) {
    return Array(n).fill(1).map((v,i)=>v+i).filter(v=>v%2===1);
}
