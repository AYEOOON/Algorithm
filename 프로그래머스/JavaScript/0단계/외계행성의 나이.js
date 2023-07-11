// 내 풀이
function solution(age) {
    word =["a","b","c","d","e","f","g","h","i","j"];
    arr = [];
    for(let a of (age).toString()){
        arr.push(word[Math.floor(a)]);
    }
    return arr.join('');
}


// 다른사람 풀이1
// 52 -> "52" -> ["5","2"]. -> ["abcdefghij"[5], "abcdefghij"[2] ] -> "fc"
function solution(age) {
  return age
    .toString()
    .split("")
    .map((v) => "abcdefghij"[v])  // 문자열 자체도 인덱스[] 접근 가능
    .join("");
}


// 다른사람 풀이2
function solution(age) {
    let char = 'abcdefghij'
    return Array.from(age.toString()).map(t => char[+t]).join('');
}
