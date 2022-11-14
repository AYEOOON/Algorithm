#include <iostream>
#include <cstring>
using namespace std;

int main()
{
  string str1("This is the first string.");
  const string str2("Here is another one.");

  str1.replace(0,4,"Here");
  
  cout << str1 << endl;
}
