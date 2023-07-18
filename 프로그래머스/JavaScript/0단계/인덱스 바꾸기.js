// 문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.

// 내 풀이
function solution(my_string, num1, num2) {
    let arr = [...my_string];
    let tmp = arr[num1];
    arr[num1] = arr[num2];
    arr[num2] = tmp
    return arr.join('')
}


// 다른사람 풀이1(원래 풀려던 방법)
function solution(my_string, num1, num2) {
    my_string = my_string.split('');
    [my_string[num1], my_string[num2]] = [my_string[num2], my_string[num1]];  // 구조분해할당 하는 방법
    return my_string.join('');
}
