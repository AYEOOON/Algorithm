// 두 정수 num과 total이 주어집니다. 
// 연속된 수 num개를 더한 값이 total이 될 때, 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.
// 예를 들어, 연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다/


// 내 풀이
function solution(num, total) {
    var answer = [];
    var middle = Math.trunc(total/num);
    if (num%2 == 0) {
        for(let i = middle-(Math.trunc(num/2)-1); i < middle+(Math.trunc(num/2)+1); i++){
            answer.push(i)
        }
    }else{
        for(let i = middle-(Math.trunc(num/2)); i < middle+(Math.trunc(num/2)+1); i++){
            answer.push(i)
        }
    }
    return answer
}


// 다른사람 풀이
// total/num => 수열의 평균값
// num/2 => 수열의 마지막에서 중앙까지의 등차 계산 ceil와 floor를 활용 수 있는 이유는 등차가 1이기때문이다.
function solution(num, total) {
    var min = Math.ceil(total/num - Math.floor(num/2));
    var max = Math.floor(total/num + Math.floor(num/2));

    return new Array(max-min+1).fill(0).map((el,i)=>{return i+min;});
}
