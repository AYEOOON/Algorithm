#include <iostream>
using namespace std;

int main() 
{ 
  // 변수
  int month ;
  int day;
  int total = 0;
  // 입력
  cout << "월을 입력하세요: ";
  cin >> month;
  cout << "일을 입력하세요: ";
  cin >> day;
  // 각 달의 날짜 수
  int m01 = 31;
  int m02 = 28;
  int m03 = 31;
  int m04 = 30;
  int m05 = 31;
  int m06 = 30;
  int m07 = 31;
  int m08 = 31;
  int m09 = 30;
  int m10 = 31;
  int m11 = 30;
  // switch 조건문을 이용해 특정 달의 날짜 번호 계산
  switch(month)  
  {
    case 12 : total += m11;
    case 11 : total += m10;
    case 10 : total += m09;
    case 9 : total += m08;
    case 8 : total += m07;
    case 7 : total += m06;
    case 6 : total += m05;
    case 5 : total += m04;
    case 4 : total += m03;
    case 3 : total += m02;
    case 2 : total += m01;
    case 1 : total += 0;
  }
  // 결과
  total += day;
  // 출력
  cout << "이 날짜는 " << total << "번째 날입니다.";
  return 0;  
}// End main
