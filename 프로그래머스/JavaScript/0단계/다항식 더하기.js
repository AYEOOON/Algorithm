// 내 풀이
function solution(polynomial) {
    const arr1 = [];
    const arr2 = [];

    for(let a of polynomial.split(' + ')){
        if (a.includes('x')) arr1.push((a==='x')?1:Number(a.slice(0,a.length-1)))
        else arr2.push(Number(a))
    }
    let sum_arr1 = arr1.reduce((sum,curr)=>sum+curr,0);
    let sum_arr2 = arr2.reduce((sum,curr)=>sum+curr,0);

    if (sum_arr1 === 0) return String(sum_arr2);
    else if (sum_arr1 === 1 && sum_arr2 === 0) return 'x'
    else if (sum_arr1 === 1) return "x"+" + "+String(sum_arr2);
    else if (sum_arr2 === 0) return String(sum_arr1)+'x';
    else return String(sum_arr1)+'x'+' + '+String(sum_arr2);
}



// 다른사람 풀이
function solution(polynomial) {
    const arr = polynomial.split(" + ");
    const xNum = arr
                .filter(n => n.includes("x"))
                .map(n => n.replace('x', '') || '1')
                .reduce((acc, cur) => acc + parseInt(cur, 10), 0);
    const num = arr
                .filter(n => !isNaN(n))
                .reduce((acc, cur) => acc + parseInt(cur, 10), 0);

    let answer = [];
    if(xNum) answer.push(`${xNum === 1 ? "" : xNum}x`);
    if(num) answer.push(num);

    return answer.join(" + ");
}
