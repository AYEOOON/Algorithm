#include <iostream>
#include <string>
using namespace std;

int main()
{
  string str1("This is the first string.");
  const string str2("Here is another one.");

  str1.assign(str2);
  
  cout << str1 << endl;
}
