// 상자의 가로, 세로, 높이가 저장되어있는 배열 box와 주사위 모서리의 길이 정수 n이 매개변수로 주어졌을 때, 상자에 들어갈 수 있는 주사위의 최대 개수를 return 하도록 solution 함수를 완성해주세요.
// 모든 면을 n으로 나눈 몫을 곱하는 문제

// 내 풀이
function solution(box, n) {
    return ~~(box[0]/n)*~~(box[1]/n)*~~(box[2]/n);
}


// 다른사람 풀이
function solution(box, n) {
    return box.reduce((acc,v) => acc * Math.floor(v / n), 1);
}
