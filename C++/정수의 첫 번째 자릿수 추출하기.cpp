#include <iostream>
using namespace std;

int main() 
{ 
  // 변수 선언
  int number;
  // 정수 입력
  cout << "숫자를 입력해주세요: ";
  cin >> number;
  // 첫번째 자릿수 추출과 출력
  cout << "입력받은 숫자: " << number << endl;
  cout << "첫번째 자릿수: " << number%100%10;
  
  return 0;
}// End main
