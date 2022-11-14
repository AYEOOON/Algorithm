#include <iostream>
#include <cstring>
using namespace std;

int main()
{
  string str1("The time has come. ");
  const string str2("Are your ready?");

  str1.append(str2);
  
  cout << str1 << endl;
}
