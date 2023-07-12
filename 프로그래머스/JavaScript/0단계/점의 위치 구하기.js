// x 좌표 (x, y)를 차례대로 담은 정수 배열 dot이 매개변수로 주어집니다. 좌표 dot이 사분면 중 어디에 속하는지 1, 2, 3, 4 중 하나를 return 하도록 solution 함수를 완성해주세요. 

// 내 풀이
function solution(dot) {
    return (0 < dot[0] && 0 < dot[1]) ? 1 : (0 > dot[0] && 0 < dot[1]) ? 2 : (0 > dot[0] && 0 > dot[1]) ? 3 : 4;
}


// 다른사람 풀이
function solution(dot) {
    const [num,num2] = dot;  // 구조분해
    const check = num * num2 > 0;
    return num > 0 ? (check ? 1 : 4) : (check ? 3 : 2);
}
