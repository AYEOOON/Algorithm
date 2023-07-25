// 점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.
// [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
//주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.
// 점은 무조건 4개씩 주어지므로, 2개씩 이었을 때 선분 조합의 경우는 4C2 (즉, 3개)
// 즉, (1-2번점과 3-4번점), (1-3번점과 2-4번점), (1-4번점과 2-3번점)이 이어졌을 경우를 계산하자


// 내 풀이
function solution(dots) {
    const [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots
    let answer1 = ((y1-y2)*(x3-x4)) == ((y3-y4)*(x1-x2));
    let answer2 = ((y1-y3)*(x2-x4)) == ((y2-y4)*(x1-x3));
    let answer3 = ((y2-y3)*(x1-x4)) == ((y1-y4)*(x2-x3));
    return answer1 || answer2 || answer3 ? 1 : 0
}


// 다른사람 풀이
function solution(dots) {
    if (calculateSlope(dots[0], dots[1]) === calculateSlope(dots[2], dots[3]))
        return 1;
    if (calculateSlope(dots[0], dots[2]) === calculateSlope(dots[1], dots[3]))
        return 1;
    if (calculateSlope(dots[0], dots[3]) === calculateSlope(dots[1], dots[2]))
        return 1;
    return 0;
}

function calculateSlope(arr1, arr2) {
    return (arr2[1] - arr1[1]) / (arr2[0] - arr1[0]);  기울기
}
