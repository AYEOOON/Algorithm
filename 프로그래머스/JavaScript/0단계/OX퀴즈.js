// 덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다.
// 수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.


// 내 풀이
function solution(quiz) {
    let arr = []
    let result = [];
    for(let i = 0; i < quiz.length; i++){
        arr.push(quiz[i].split("="))
        if (eval(arr[i][0]) === eval(arr[i][1])) result.push("O")
        else result.push("X")
    }
    return result
}


// 다른사람 풀이
function solution(quiz) {
  return quiz
    .map((el) => el.split(" = "))
    .map((el) => {
      return eval(el[0]) == el[1] ? "O" : "X";
    });
}
