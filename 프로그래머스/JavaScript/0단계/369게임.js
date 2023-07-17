// 내 풀이
function solution(order) {
    let num = ['3','6','9']
    var answer = 0;
    let arr = String(order).split('')
    for(let a of arr){
        if (num.includes(a)) answer += 1;
    }
    return answer;
}


// 다른사람 풀이
function solution(order) {
    return (''+order).split(/[369]/).length-1; // 3,6,9를 빼면 공백생김, 공백도 센 뒤 -1
}
