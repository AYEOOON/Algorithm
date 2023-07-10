// 별출력하는 문제
// readline모듈에 관해서 알게되었다.
// https://lakelouise.tistory.com/140


// 내 풀이
const readline = require('readline');  // 모듈 가져오기
const rl = readline.createInterface({  //readline 모듈을 이용해 입출력을 위한 인터페이스 객체 생성
    input: process.stdin,
    output: process.stdout
});

//rl 변수
rl.on('line', function (line) {  // 한 줄씩 입력받은 후 실행할 코드
    input = line;   // 입력된 값은 line에 저장된다. 
}).on('close', function () {   
    let InputNum = Number(input);  // 입력이 끝난 후 실행할 코드 
    for (let i = 1; i <= InputNum; i++){
        console.log('*'.repeat(i));
    }
});
