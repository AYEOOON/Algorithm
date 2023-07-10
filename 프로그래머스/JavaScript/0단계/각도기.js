// 내 풀이
function solution(angle) {
    return  ((0 < angle) && (angle< 90)) ? 1 : (angle == 90) ? 2 :((90 < angle) && (angle < 180)) ? 3 : 4;
}

// 내 풀이를 개선한 풀이
function solution(angle) {
    return angle < 90 ? 1 : angle === 90 ? 2 : angle < 180 ? 3 : 4;
}


// 다른사람 풀이
function solution(angle) {
    return [0, 90, 91, 180].filter(x => angle>=x).length;
}
