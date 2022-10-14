// 해야할 것: 주석달기

#include <iostream>
#include <iomanip>
using namespace std;

void rowTransform (const int originArray [][4], int rowSize, int rowArray[])
{
  int i = 0;
  int j = 0;
  for (int k = 0; k < 8; k++)
  {
    rowArray[k] = originArray[i][j];
    j++;
    if(j > 3)
    {
      i++;
      j = 0;
    }
  }
}
void colTransform(const int originArray[][4], int rowSize, int colArray[])
{
  int i = 0;
  int j = 0;
  for(int k = 0; k<8; k++)
  {
    colArray[k] = originArray[i][j];
    i++;
    if(j>1)
    {
      j++;
      i=0;
    }
  }
}
void printTwoDimensional(const int twoDimentional[][4], int rowSize)
{
  for(int i = 0; i < rowSize; i++)
  {
    for(int j = 0; j < 4; j++)
    {
      cout << setw(4) << twoDimentional[i][j];
    }
    cout << endl;
  }
  cout << endl;
}
void printOneDimensional(const int oneDimensional[], int size)
{
  for(int i = 0; i < size; i++)
  {
    cout << setw(4) << oneDimensional[i];
  }
  cout << endl;
}
int main()
{
  
  int originArray[2][4] = {{0, 1, 2, 3},{10, 11, 12, 13}};
  int rowArray[8];
  int colArray[8];

  rowTransform(originArray, 2, rowArray);
  colTransform(originArray, 2, colArray);

  cout << "Origin Array " << endl;
  printTwoDimensional(originArray, 2);

  cout << "Row-Trnasformed Array : ";
  printOneDimensional(rowArray, 8);

  cout << "Column-Transformed Array : ";
  printOneDimensional(colArray, 8);

  return 0;
}
