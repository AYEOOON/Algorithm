// 내 풀이
function solution(name, yearning, photo) {
    const arr = [];
    const answer = [];
    for (let i = 0; i < name.length; i++){
        arr[name[i]] = yearning[i];
    }
    for (ph of photo){
        let cnt = 0;
        for (p of ph){
            if (p in arr){
                cnt+=arr[p];
            }
        }
        answer.push(cnt);
    }
    return answer;
}

// 내 풀이 개선하기
// 해시보다 Map 객체를 사용
function solution(name, yearning, photo) {
    // 1. 이름과 그리움 점수를 매핑하는 Map 생성 (초기화)
    const nameYearningMap = new Map();
    for (let i = 0; i < name.length; i++) {
        nameYearningMap.set(name[i], yearning[i]); // Map에 이름과 점수 추가
    }

    const answer = [];

    // 2. 각 사진에 대해 반복
    for (const ph of photo) {
        let currentPhotoScore = 0;
        // 3. 현재 사진 안의 각 인물에 대해 반복
        for (const personName of ph) {
            // 4. Map.get()으로 그리움 점수 가져오기. 이름이 없으면 ?? 0 (0으로 기본값 설정)
            currentPhotoScore += nameYearningMap.get(personName) ?? 0;
        }
        answer.push(currentPhotoScore);
    }

    return answer;
}


// 다른사람 풀이
function solution(name, yearning, photo) {
    return photo.map((v)=> v.reduce((a, c)=> a += yearning[name.indexOf(c)] ?? 0, 0))
}
/*
1. photo.map((v) => ...) : photo 배열 안의 각 사진들에 대해 반복
2. v.reduce((a, c) => a += yearning[name.indexOf(c)] ?? 0, 0): 각 사진의 점수를 게산
  - v.reduce(): 현재 사진 안의 이름 반복
  - a: 누산기
  - c: 현재 처리 중인 이름
  - name.indexOf(c): 이름에 대한 인덱스
  - yearning[name.indexOf(c)]: 위에서 구한 인덱스의 점수
  - ?? 0: 만약 이름이 없는 경우 0으로 사용
  - ,0: 시작 점수 (a의 시작 값)
*/
