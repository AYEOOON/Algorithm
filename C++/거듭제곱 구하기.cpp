#include <iostream>

using namespace std;

int main()
{ 
  // 변수 선언
  int base;
  int exponent;
  int power, counter;
  // 입력
  do
  {
    cout << "밑을 입력해주세요: ";
    cin >> base;
    cout << "지수를 입력해주세요: ";
    cin >> exponent;
  } while(exponent < 0);
  // 초기화
  power = 1;
  counter = 0;
  // counter가 exponent보다 작은 경우 반복
  for(int i = 1; i <= exponent; i++)
  {
    power *= base;
  }
  // 출력
  cout << base << "의 " << exponent << "승은 " << power << "입니다.";
  return 0;
}
