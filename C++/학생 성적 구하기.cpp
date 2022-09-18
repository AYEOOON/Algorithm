#include <iostream>
#include <algorithm>
using namespace std;

int main() 
{ 
  // Declaration
  int score1, score2, score3;
  int maxScore, minScore;
  int average;
  // input
  cout << "점수를 입력하세요: ";
  cin >> score1;
  cin >> score2;
  cin >> score3;
  // Decision making
  maxScore = max({score1, score2, score3});
  minScore = min({score1, score2, score3});
  average = (maxScore+minScore)/2;
  // Output
  cout << "Score? " << score1 << score2 << score3 << endl;
  cout << "최대와 최소는: " << maxScore << minScore << endl;
  cout << "성적은: " << average;
  return 0;
}// End main
