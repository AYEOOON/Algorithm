// my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.

// 내 풀이
function solution(my_string) {
    var answer = [];
    for(let a of my_string){
        if(answer.includes(a)){
            continue
        }else{
            answer.push(a)
        }
    }
    return answer.join('')
}

// 다른사람 풀이
// 파이썬에서는 순서가 사전순으로 정렬되지만, js에서는 순서가 의미없다.
function solution(my_string) {
    return [...new Set(my_string)].join('');  // my_string을 split()으로 굳이 나눌 필요 없이 바로 인자로 전달
}
