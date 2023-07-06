
// 내 풀이
function solution(money) {
    americano = ~~(money/5500);
    change = money - (~~(money/5500)*5500);
    var answer = [americano, change];
    return answer;
}

// 개선한 내 풀이
function solution(money) {
    return answer = [~~(money/5500), money - (~~(money/5500)*5500)];
}

// 다른사람 풀이
function solution(money) {
    return [~~(money / 5500), money % 5500];
}
