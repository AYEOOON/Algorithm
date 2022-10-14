#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
  // 선언과 초기화
  const int CAPACITY = 10;
  int frequencies [CAPACITY] = {0};
  ifstream integerFile;
  // 정수 파일 열기
  integerFile.open ("integerFile.dat");
  if (!integerFile)
  {
    cout << "[ERROR] 파일을 찾을 수 없습니다!";
    return 0;
  }
  // 파일에서 정수를 읽고, 빈도 배열 작성
  int data;
  int size = 0;
  while (integerFile >> data)
  {
    if (data >= 0 && data <= 9)
    {
      size++;
      frequencies[data]++;
    }
  }
  // 정수 파일 닫기
  integerFile.close();
  // 빈도 배열과 히스토그램 출력
  cout << "There are " << size << " valid data items." << endl;

  for(int i = 0; i < 10; i++)
  {
    cout << setw(3) << i << " ";

    for(int f = 1; f <= frequencies[i]; f++)
    {
      cout << '*';
    }
    cout << " " << frequencies[i] << endl;
  }
  return 0;
}
