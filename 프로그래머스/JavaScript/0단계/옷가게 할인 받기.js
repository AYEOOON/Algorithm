// 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
// 구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.

// 내 풀이
function solution(price) {
    if ((100000 <= price) && (price < 300000)){
        return Math.trunc(price * 0.95);
    }
    else if ((300000 <= price) && (price < 500000)){
        return Math.trunc(price * 0.9);
    }
    else if (500000 <= price){
        return Math.trunc(price * 0.8);
    }
    else{
        return Math.trunc(price);
    }
}


// 다른사람 풀이
function solution(price) {
    return price>=500000 ? parseInt(price*8/10) : (price>=300000 ? parseInt(price*9/10) : (price >= 100000 ? parseInt(price*19/20) : price))
}
