/* 1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

1. 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
2. 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
3. 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
4. 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.

네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.
*/
// 가끔 단순 노동이 나은 풀이가 된다는 것을 깨닫게 됨


// 내 풀이
function solution(a, b, c, d) {
    const arr = [a,b,c,d];
    if ([...new Set(arr)].length === 4) return Math.min(...arr)
    
    var count = {};
    for(const num of arr){
        count[num] = arr.filter(el => el === num).length
    }
    if ([...new Set(arr)].length === 1) return 1111*arr.pop()
    if ([...new Set(arr)].length === 2){
        if (Object.values(count).includes(3)){
            let p = Object.keys(count).find((p) => count[p] === 3)
            let q = Object.keys(count).find((p) => count[p] === 1)
            return (10 * Number(p) + Number(q))**2
        }
        else{
            let [p, q] = Object.keys(count)
            return (Number(p) + Number(q)) * Math.abs(Number(p) - Number(q))
        }
    }
    else{
        let p = Object.keys(count).find((p) => count[p] === 2)
        let [q,r] = Object.keys(count).filter((p) => count[p] === 1)
        return Number(q)*Number(r)
    }
}



// 다른사람 풀이
function solution(a, b, c, d) {
    if (a === b && a === c && a === d) return 1111 * a

    if (a === b && a === c) return (10 * a + d) ** 2
    if (a === b && a === d) return (10 * a + c) ** 2
    if (a === c && a === d) return (10 * a + b) ** 2
    if (b === c && b === d) return (10 * b + a) ** 2

    if (a === b && c === d) return (a + c) * Math.abs(a - c)
    if (a === c && b === d) return (a + b) * Math.abs(a - b)
    if (a === d && b === c) return (a + b) * Math.abs(a - b)

    if (a === b) return c * d
    if (a === c) return b * d
    if (a === d) return b * c
    if (b === c) return a * d
    if (b === d) return a * c
    if (c === d) return a * b

    return Math.min(a, b, c, d)
}
