// 선분 3개가 평행하게 놓여 있습니다. 
// 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때, 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.


// 내 풀이
function solution(lines) {
    const start = Math.min(...lines.flat());  //  최초로 그려지는 선분의 시작점
    const end = Math.max(...lines.flat());   // 마지막에그려지는 선분의 종단점
    const arr = new Array(end-start).fill(0)  // 그 차이만큼 0으로 채워진 리스트생성
    lines.forEach((el)=>{
        for(let i = el[0]; i < el[1]; i++)
            arr[i-start] += 1  // 각 선분들의 길이를 idx에 대입하여 1씩 더해준다.
    })
    return arr.filter(el => el>=2).length  // 리스트에 2이상인 부분을 필터링
}


// 다름사람 풀이
function solution(lines) {
    let line = new Array(200).fill(0);

    lines.forEach(([a, b]) => {
        for(; a < b; a++) line[a+100]++;
    });

    return line.reduce((a, c) =>  c > 1 ? a + 1 : a, 0)
}
