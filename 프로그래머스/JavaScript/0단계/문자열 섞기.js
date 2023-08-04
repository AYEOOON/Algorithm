// 길이가 같은 두 문자열 str1과 str2가 주어집니다.
// 두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.


// 내 풀이
function solution(str1, str2) {
    let arr = [];
    let answer = '';
    for(i in str1){
        answer += str1[i]
        answer += str2[i]
    }
    return answer
}

// 다른사람 풀이
function solution(str1, str2) {
    return [...str1].map((x, idx)=> x+str2[idx]).join("");
}
