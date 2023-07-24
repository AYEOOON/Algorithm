// 지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
// 지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

// 내 풀이
function solution(board) {
    const dx = [1, 0, -1, 0, 1, 1, -1, -1];
    const dy = [0, 1, 0, -1, 1, -1, 1, -1];
    
    const danger = [];
    for(let i = 0; i < board.length; i++){
        for(let j = 0; j < board.length; j++){
            if(board[i][j] === 1) danger.push([i,j])
        }
    }
    danger.forEach((w)=>{
        for (let i = 0; i < 8; i++){
            const nx = w[0]+dx[i];
            const ny = w[1]+dy[i];
            
            if (nx >= 0 && ny >= 0 && nx < board.length && ny < board.length && board[nx][ny] === 0){
                board[nx][ny] = 1;
            }
        }
    })
    let safe = 0;
    for(let i = 0; i < board.length; i++){
        for(let j = 0; j < board.length; j++){
            if(board[i][j] === 0) safe += 1
        }
    } 
    return safe
}



// 다른사람 풀이
function solution(b) {
    const directions = [[0,0],[0,1],[0,-1],[1,1],[1,0],[1,-1],[-1,-1],[-1,0],[-1,1]]
    let bombSet = new Set();

    for(let i = 0; i < b.length; i++) {
        for(let j = 0; j < b[i].length; j++) {
            if(b[i][j] == 1) {
                directions.forEach(el => {
                    let [nextX, nextY] = el;
                    [nextX, nextY] = [i+nextX, j+nextY];
                    if(nextX >= 0 && nextX < b.length && nextY >= 0 && nextY < b[i].length) {
                        bombSet.add(nextX+' '+nextY);
                    }
                })
            }
        }
    }
    return b.length * b[0].length - bombSet.size;
}
