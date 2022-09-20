#include <iostream>
using namespace std;

int main() 
{ 
  // 변수 선언
  int time;
  int sec,min,hr;
  // 초 단위의 정수 입력
  cout << "초를 입력해주세요: ";
  cin >> time;
  sec = time;
  // 입력받은 초를 시,분,초로 바꿈
  hr = sec/3600;
  min = sec%3600/60;
  sec = sec%3600%60;
  // 시,분,초 출력
  cout << "입력받은 초: " << time << endl;
  cout << "입력받은 시간은 " << hr << "시간 " << min << "분 " << sec << "초입니다!";
  
  return 0;
}// End main
