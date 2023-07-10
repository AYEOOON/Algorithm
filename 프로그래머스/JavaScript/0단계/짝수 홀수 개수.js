// num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

// 내 풀이
function solution(num_list) {
    let odd = 0;
    let even = 0;
    for(let num of num_list){
        if (num%2==0){
            even += 1;
        }else{
            odd += 1;
        }
    }
    return [even, odd];
}

// 개선한 내 풀이
function solution(num_list) {
    let odd = 0;
    let even = 0;
    for(let num of num_list){
        num%2 ? odd+=1 : even+=1;
    }
    return [even, odd];
}


// 다른사람 풀이1
function solution(num_list) {
    var answer = [0,0];

    for(let a of num_list){
        answer[a%2] += 1  // 짝수 홀수의 나머지를 인덱스로 활용
    }

    return answer;
}


// 다른사람 풀이2
function solution(num_list) {
  return [
    num_list.filter((num) => num % 2 === 0).length,
    num_list.filter((num) => num % 2 === 1).length,
  ];
}
