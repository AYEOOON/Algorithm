// 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 
// 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.


// 내 풀이
function solution(babbling) {
    let result = 0
    const answer = []
    babbling.forEach((el)=>{
        el = el.replace("aya", "1");
        el = el.replace("ye", "1");
        el = el.replace("woo", "1");
        el = el.replace("ma", "1");
        answer.push(el)
    })
    answer.forEach((el)=>{
        var regex = /^-?\d+$/;
        if(regex.test(el)) result += 1
    })
    return result
}


// 다른사람 풀이
function solution(babbling) {
  var answer = 0;
  const regex = /^(aya|ye|woo|ma)+$/;

  babbling.forEach(word => {
    if (regex.test(word)) answer++;  
  })

  return answer;
}
