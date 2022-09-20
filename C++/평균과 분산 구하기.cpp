#include <iostream>
#include <cmath>
using namespace std;

int main() 
{ 
  // 변수 선언
  int num1, num2, num3;
  int sum, avg, vri; 
  // 숫자 입력
  cout << "숫자 3개를 입력해주세요: ";
  cin >> num1 >> num2 >> num3;
  // 총합, 평균, 분산 구하기
  sum = num1 + num2 + num3;
  avg = sum/3;
  vri = (pow(avg-num1,2)+pow(avg-num2,2)+pow(avg-num3,2))/3;    // 분산인지 편차인지 교수님께,,여줘보기
  // 출력
  cout << "총합: " << sum << endl;
  cout << "평균: " << avg << endl;
  cout << "분산: " << vri << endl;
  
  return 0;
}// End main
