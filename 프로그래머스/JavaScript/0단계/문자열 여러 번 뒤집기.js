// 문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다. 
// queries의 원소는 [s, e] 형태로, my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다.
// my_string에 queries의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.

// slice: slice() 메소드는 begin부터 end 전까지의 복사본을 새로운 배열 객체로 반환(원본배열 수정X)
// splice: splice() 함수를 사용하면 원본 배열인 arr이 변경


// 내 풀이
function solution(my_string, queries) {
    queries.forEach(a=> {
        const copyarr = [...my_string]
        const slice = copyarr.slice(a[0],a[1]+1).reverse().join("")
        copyarr.splice(a[0], a[1]-a[0]+1, slice)
        my_string = copyarr.join('')
    })
    return my_string
}


// 다른사람 풀이
function solution(my_string, queries) {
    let str = my_string.split('');
  queries.forEach(([start, end]) => {
    const changeStr = str.slice(start, end + 1);
    str.splice(start, changeStr.length, ...changeStr.reverse());
  });
  return str.join('');
}
