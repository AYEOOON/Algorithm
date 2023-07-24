// my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

// 내 풀이
function solution(my_string) {
    return my_string.split(/[a-zA-Z]/g).map(el => Number(el)).reduce((sum,cur) => sum+cur)
}


// 다른사람 풀이
function solution(my_string) {
  return my_string.split(/\D+/).reduce((acc, cur) => acc + Number(cur), 0);  // \D : 숫자가 아닌 문자에 대한 전역 검색을 수행
}
