#include <iostream>
using namespace std;

int main()
{ 
    // 변수 선언
    bool success = false;
    int size;
    int item;
    // 입력
    do
    {
        cout << "입력할 횟수를 입력해주세요: ";
        cin >> size;    
    } while(size < 0);
    // counter가 size보다 작은 경우 반복
    for(int i = 0; (i < size) && (!success); i++)
    {
        cout << "숫자를 입력하세요: ";
        cin >> item;
        success = (item % 5==0);
    }
    // 성공하는 조건
    if(success)
    {
        cout << item << "은/는 5로 나눌 수 있습니다." << endl;
    }
    else
    {
        cout << "숫자들 중에 5로 나눌 수 있는 수가 없습니다." << endl;
    }
    return 0;
}
