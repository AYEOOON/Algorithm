// strlist 각 원소의 길이를 담은 배열을 retrun하도록 solution 함수를 완성해주세요.

// 내 풀이
function solution(strlist) {
    var answer = [];
    for(let a of strlist){
        answer.push(a.length)
    }
    return answer;
}


// 다른사람 풀이
function solution(strlist) {
    return strlist.map((el) => el.length)  // 배열 돌면서 특정행위를 할 때는 map사용
}
