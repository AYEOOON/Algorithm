// 나이 age가 주어질 때, 2022년을 기준 출생 연도를 return 하는 solution 함수를 완성해주세요.


// 내 풀이
function solution(age) {
    return answer = 2022-age+1;
}


// 다른사람풀이(만약 기준이 2022년이 아닌 그때의 해로 정한다면)
function solution(age) {
    return new Date().getFullYear() - age + 1;
}
