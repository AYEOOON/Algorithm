// 공은 1번부터 던지며 오른쪽으로 한 명을 건너뛰고 그다음 사람에게만 던질 수 있습니다. 
// 친구들의 번호가 들어있는 정수 배열 numbers와 정수 K가 주어질 때, k번째로 공을 던지는 사람의 번호는 무엇인지 return 하도록 solution 함수를 완성해보세요.


// 내 풀이
// 공을 받는 사람 순서를 찾습니다. (k * 2)
// 공을 던지는 사람 순서로 변경합니다. ((K -1) * 2)
// 순환되는 구조이므로 나머지를 통해 위치를 찾습니다. % numbers.length
function solution(numbers, k) {
    return numbers[((k-1)*2)%numbers.length];
}


// 다른사람 풀이
function solution(numbers, k) {
    return numbers[(--k*2)%numbers.length];   //k-1 후 2를 곱한 만큼 움직임, 움직이는 거리가 배열의 길이를 초과한 경우를 위해 배열길이로 모듈러연산
}
