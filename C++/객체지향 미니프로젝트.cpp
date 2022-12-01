// product.h

#ifndef PRODUCT_H
#define PRODUCT_H
#include <iostream>
using namespace std;



class Product 
{
  private:
    string name;
    int price;
  public:
    Product(string name, int price);
    ~Product();
    void print() const;

};
#endif

// product.cpp

#include "product.h"

Product ::Product(string nm, int pr)
: name(nm), price(pr)
{
}

Product::~Product()
{
}




// serch()
string search;
  int offset;
  string line;
  ifstream istr;
  istr.open("Product_List");

  cout << "찾으시는 제품의 이름을 입력하세요: " << endl;
  cin >> search;

  if (istr.is_open())
  {
    while(!istr.eof())
    {
      getline(istr,line); 
      if((offset = line.find(search,0))!=string::npos)
        cout << "해당 제품을 찾았습니다." << search << endl;
    }
    istr.close();
  }
  else
  {
    cout << "해당 제품을 찾지 못했습니다." << endl;

    system("pause");
    
void Product::print() const
{
  cout << "-----------------------" << endl;
  cout << "NAME: " << name << endl;
  cout << "PRICE(krw): " << price << endl;
}

// app.cpp

#include "product.h"

int main()
{
  Product Product1("RED STAND", 24000);
  Product1.print();

  Product Product2("WOOD CHAIR", 56000);
  Product2.print();

  Product Product3("WHITE CURTAIN", 13000);
  Product3.print();

  Product Product4("NAVY COUCH", 113000);
  Product4.print();

  Product Product5("SQUARE TRASH CAN", 9900);
  Product5.print();

}
