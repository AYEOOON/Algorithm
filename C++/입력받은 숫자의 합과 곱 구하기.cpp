#include <iostream>
#include <iomanip>
using namespace std;

int main()
{ 
  // 변수 선언
  int size;
  long double number;
  long double sum,product;
  // 입력
  do
  {
    cout << "음이 아닌 정수를 입력해주세요: ";
    cin >> size;
  } while (size < 0);
  // 초기화
  sum = 0;
  product = 1;
  // counter가 size보다 작은 경우 반복
  for(int i = 1; i <= size; i++)
  {
    cout << "다음 숫자를 입력하세요: ";
    cin >> number;
    sum += number;
    product *= number;
  }
  // 출력
  cout << fixed << setprecision(2);
  cout << "합 = " << sum << endl;
  cout << "곱 = " << product;
  return 0;
}
