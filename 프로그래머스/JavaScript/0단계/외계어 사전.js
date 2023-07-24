// 알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어집니다. 
// spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.
// 못풂


// 풀이1 
function solution(spell, dic) {
    const arr = [];
    dic.forEach((word)=>{   // dic 배열의 원소 하나에 대하여 spell을 검사
        let count = 0;
        spell.forEach((el)=>{
            if(word.includes(el)) count += 1  // 만약, spell의 원소가 포함되어 있다면 count를 증가
            
        })
        if (count === spell.length) arr.push(word)  // 하나의 dic 배열 원소에 대한 연산이 끝날 때, count가 spell 배열의 길이와 같다면 배열에 해당 dic 원소를 넣는다.
    })
    return arr.length === 0 ? 2 : 1
    
}


// 풀이2
// every()는 배열이 주어진 조건을 모두 통과하는지를 판단하여 boolean 값을 반환
// spell에 있는 모든 원소가 dic의 배열 원소 하나에 포함돼야 true를 반환
function solution(spell, dic) {
    return dic.filter(v=>spell.every(c=>v.includes(c))).length ? 1 : 2;
}
