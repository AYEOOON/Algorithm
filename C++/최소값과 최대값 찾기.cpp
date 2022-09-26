#include <iostream>
#include <limits>
using namespace std;

int main()
{ 
  // 변수 선언
  int size;
  int smallest, largest;
  int counter, number;
  // 입력
  do
  {
    cout << "입력할 횟수를 입력해주세요: ";
    cin >> size;
  } while(size <= 0);
  // 초기화
  smallest = numeric_limits<int>::max();
  largest = numeric_limits<int>::min();
  counter = 0;
  // counter가 size보다 작은 경우 반복
  for(int i = 1; i <= size; i++)
  {
    cout << "숫자를 입력하세요: ";
    cin >> number;
    if (smallest > number)
    {
      smallest = number;
    }
    else if (largest < number)
    {
      largest = number;
    }
  }
  // 출력
  cout << "최소값: " << smallest << endl;
  cout << "최대값: " << largest;
  return 0;
}
