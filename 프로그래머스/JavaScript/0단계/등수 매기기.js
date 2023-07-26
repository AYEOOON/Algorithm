// 영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때, 영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.

// 내 풀이
function solution(score) {
    const answer = [];
    const arr = score.map(el => el.reduce((sum,cur) => sum+cur)/2).map(el=> String(el))
    const sort_arr = score.map(el => el.reduce((sum,cur) => sum+cur)/2).sort((a,b)=>b-a)
    arr.forEach((el)=>{
        answer.push(sort_arr.indexOf(Number(el))+1)
    })
    return answer
}


// 다른사람 풀이1
function solution(score) {
  return score.map((el) => {
    return (
      score.filter((v) => (v[0] + v[1]) / 2 > (el[0] + el[1]) / 2).length + 1  // 자기보다 점수가 높은사람 수+1
    );
  });
}


// 다른사람 풀이2
function solution(score) {
    let avg = score.map(v=>(v[0]+v[1])/2);
    let sorted = avg.slice().sort((a,b)=>b-a);
    return avg.map(v=>sorted.indexOf(v)+1);
}
