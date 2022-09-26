#include <iostream>
using namespace std;

int main()
{ 
  // 변수 선언
  int size;
  bool success = false;
  int item;
  // 입력
  do
  {
    cout << "크기를 입력해주세요: ";
    cin >> size;    
  } while(size < 0);
  // counter가 size보다 작은 경우 반복
  for(int i = 1; (i < size) && (!success); i++)
  {
    cout << "숫자를 입력하세요: ";
    cin >> item;
    
  }
  return 0;
}
