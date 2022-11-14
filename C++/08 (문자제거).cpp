#include <iostream>
#include <string>
using namespace std;

int main()
{
  string str("This is a long string.");
  
  int p = str.find("is");

  cout << str[p] << endl;
}
