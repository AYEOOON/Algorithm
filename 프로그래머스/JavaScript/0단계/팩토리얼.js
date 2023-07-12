// 정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.

// 내 풀이
function solution(n) {
    let sum = 1;
    for(let i = 1; i <= 10; i++){
        sum *= i;
        if(n === sum) return i;
        if(n < sum) return i - 1;
    }
}

// 다른사람 풀이1
let solution=n=>10-[0,1,2,6,24,120,720,5040,40320,362880,3628800,n].sort((a,b)=>a-b).reverse().indexOf(n)


// 다른사람 풀이2(재귀)
function factorial(n){
    if (n <= 1){
        return 1;
    }
    else{
        return n*factorial(n-1);    
    }
}

function solution(n) {
    for(let i = 1; i<12; i++){
        if (factorial(i) > n){
            return i-1;
        }
    }
}
