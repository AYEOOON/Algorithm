// 자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
// 접근 방식은 맞았지만 풀지못함

// 풀이
function solution(n) {
    let answer =[];  // i가 들어갈 배열
    let i = 2;  // 소인수 분해가 되는 가장 작은 값을 선언
    while(n>=2){   // n이 2가 될 수 있기 때문에 2로 설정
        if(n%i === 0) {  // 나눠지는 경우: i의 모든 배수를 제거하여 소인수만 남도록 함
            answer.push(i) 
            n = n/i;
        }else{
        i++;
        }
    }
    return [...new Set(answer)];  // 중복된 값 제거
}
