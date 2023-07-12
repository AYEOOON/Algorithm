// 정수 배열 num_list와 정수 n이 매개변수로 주어집니다. num_list를 다음 설명과 같이 2차원 배열로 바꿔 return하도록 solution 함수를 완성해주세요.
  

// 내 풀이
function solution(num_list, n) {  
    var answer = [];
    for(let i = 0; i<num_list.length/n; i++){   // num_list 배열 길이에서 n을 나눈 몫만큼 반복
        answer.push(num_list.slice(i*n,i*n+n)); // slice 배열 내장 함수는 index를 통해서 배열을 자르고 자른 배열을 return
    }                                           // 첫번째 인자로 자르기 시작하는 index를 받고, 두번째 인자로 어디 index 전까지 자를지 해당 index를 넣어주면 된다.
    return answer;
}



// 다른사람 풀이
function solution(num_list, n) {
    var answer = [];

    while(num_list.length) {
        answer.push(num_list.splice(0,n));   //splice 메서드 반환값이랑 원본배열 변경하는 것 기억
    }

    return answer;
}
