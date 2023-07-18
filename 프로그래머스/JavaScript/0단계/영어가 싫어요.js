// 영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 문자열 numbers가 매개변수로 주어질 때, numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.


// 내 풀이
function solution(numbers) {
    const num = {
        "zero":0,
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
    };
    for(const a in num){
        numbers = numbers.replaceAll(a, String(num[a]))  // replace를 replaceAll로 바꾸니 통과됨
    }
    return Number(numbers)
}


// 다른사람 풀이1
function solution(numbers) {
    const obj = {
        zero: 0, one: 1, two: 2, three: 3, four: 4,
        five: 5, six: 6, seven: 7, eight: 8, nine: 9
    };

    // replace 두번째 인자를 콜백으로 할수도 있다.
    const num = numbers.replace(/zero|one|two|three|four|five|six|seven|eight|nine/g, (v) => {
        return obj[v];
    });

    return Number(num);
}


// 다른사람 풀이2
// reduce에서 인덱스로 받아올 수 있다. 
var solution=n=>Number(['zero','one','two','three','four','five','six','seven','eight','nine'].reduce((t,s,i)=>t.replaceAll(s,i),n))
