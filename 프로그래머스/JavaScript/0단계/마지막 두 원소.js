// 정수 리스트 num_list가 주어질 때, 
// 마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을 
// 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여 return하도록 solution 함수를 완성해주세요.


// 내 풀이
function solution(num_list) {
    if(num_list[num_list.length-1] > num_list[num_list.length-2]) num_list.push(num_list[num_list.length-1] - num_list[num_list.length-2])
    else num_list.push(num_list[num_list.length-1] *2)
    return num_list
}



// 다른사람 풀이
function solution(num_list) {
    const [a, b] = [...num_list].reverse();   // 배열을 반대로 뒤집은 뒤, 구조분해할당 후 0번째와 1번째 크기 비교
    return [...num_list, a > b ? (a-b):a*2];  // 배열 풀어서 조건 추가
}
