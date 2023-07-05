# 피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.

# 내 풀이
function solution(n) {
    if(n%7===0){
        return Math.trunc(n/7)   # 소수점 이하는 버리는 함수사용
    }else{
        return Math.trunc(n/7)+1
    }
}

function solution(n) {
    return Math.ceil(n / 7)  # 인수와 같거나 큰 수 중에서 가장 작은 정수 반환
}
