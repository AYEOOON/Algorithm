/*
https://school.programmers.co.kr/learn/courses/30/lessons/68936

[문제 설명]
2차원 배열을 쿼드 트리(Quad Tree) 방식으로 압축한 후, 최종적으로 남는 0과 1의 개수를 구하는 문제이다.
현재 영역의 모든 값이 같다면 해당 영역을 하나의 숫자로 압축한다. 값이 하나라도 다르다면 영역을 4등분하여 같은 과정을 반복한다.

[풀이 아이디어]
이 문제는 분할 정복(Divide and Conquer) 을 활용하여 해결하였다.

현재 탐색 중인 영역이 모두 같은 값인지 확인하고, 모두 같다면 해당 값을 압축된 결과로 카운트한다. 
만약 다른 값이 존재한다면 현재 영역을 4개의 동일한 크기의 정사각형으로 분할한 뒤 각 영역에 대해 동일한 작업을 재귀적으로 수행한다.

배열을 직접 복사하여 4등분하지 않고, 시작 좌표 (x, y) 와 현재 영역의 한 변 길이 size 를 전달하는 방식으로 구현하였다. 
이를 통해 불필요한 배열 생성 없이 원하는 영역만 탐색할 수 있다.

isSame() 메서드는 현재 영역이 모두 동일한 값으로 이루어져 있는지 검사하며, 
quad() 메서드는 압축 가능 여부를 판단한 후 압축하거나 4개의 하위 영역으로 분할하는 역할을 수행한다.

재귀 호출이 모두 종료되면 압축된 0의 개수와 1의 개수가 answer 배열에 저장된다.

[동작 과정]
1. 현재 영역이 모두 같은 값인지 확인한다.
2. 모두 같다면 해당 숫자의 개수를 증가시킨다.
3. 값이 다르다면 현재 영역을 4등분한다.
4. 각 영역에 대해 다시 1~3 과정을 반복한다.
5. 모든 재귀 호출이 종료되면 압축된 0과 1의 개수를 반환한다.

[시간 복잡도]
최악의 경우 모든 영역을 끝까지 분할하며 탐색하므로 시간 복잡도는 O(N² log N) 수준으로 볼 수 있다. 
다만 실제로는 압축이 가능한 영역에서 탐색이 조기에 종료되므로 평균적으로는 더 적은 연산으로 해결된다.
*/

class Solution {
    int[] answer = new int[2];
    public int[] solution(int[][] arr) {
        quad(arr, 0, 0, arr.length);
        return answer;
    }
    
    public int[] quad(int[][] arr, int x, int y, int size){
        if (isSame(arr, x, y, size)){
            if (arr[x][y] == 0){
                answer[0]++;
            }else{
                answer[1]++;
            }
        }else{
            int half = size / 2;
            quad(arr, x, y, half);
            quad(arr, x, y+half, half);
            quad(arr, x+half, y, half);
            quad(arr, x+half, y+half, half);
        }
        return answer;
    }
    
    public boolean isSame(int[][] arr, int x, int y, int size){
        int value = arr[x][y];
        
        for (int i = x; i < x+size; i++){
            for (int j = y; j < y+size; j++){
                if (value != arr[i][j]){
                    return false;
                }
            }
        }
        return true;
    }
}
