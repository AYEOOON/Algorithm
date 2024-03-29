// 1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다. 정수 i, j, k가 매개변수로 주어질 때, i부터 j까지 k가 몇 번 등장하는지 return 하도록 solution 함수를 완성해주세요.

// 내 풀이
function solution(i, j, k) {
    const arr = [];
    for (let n = i; n <= j; n++){
        arr.push(String(n));
    }
    return arr.join('').split('').filter(el => el === String(k)).length
}


// 다른사람 풀이
function solution(i, j, k) {
    let a ='';
    for(i;i<=j;i++){
        a += i;
    }

    return a.split(k).length-1;  // k가 9라고 가정하면 '191'인 경우 9로 분리하면 '1', '1'이고 '19191'이면 '1', '1', '1' 이렇게 9의 개수보다 항상 1이 많아지므로 -1
}
