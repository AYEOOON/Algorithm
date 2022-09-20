#include <iostream>
using namespace std;

int main() 
{ 
  // 변수 선언
  double number;
  int jungsu;
  float sosujum;
  // 숫자 입력받기
  cout << "숫자를 입력해주세요: ";
  cin >> number;
  // 정수부분과 소수점 아래부분 추출
  jungsu = int(number);
  sosujum = number - jungsu;
  // 출력
  cout << "입력받은 숫자: " << number << endl;
  cout << "정수: " << jungsu << endl;
  cout << "소수점 아래: " << sosujum;
  
  return 0;
}// End main
