#include <iostream>
using namespace std;

class Circle
{
  private:
    double radius;
  public:
    double getRadius() const;
    double getArea() const;
    double getPerimeter() const;
    void setRadius(double value);
};

double Circle::getRadius() const
{
  return radius;
}

double Circle::getArea() const
{
  const double PI = 3.14;
  return(PI*radius*radius)
}

double Circle::getPerimeter() const
{
  const double PI = 3.14;
  return(2*PI*radius);
}

void Circle::setRadius(double value)
{
  radius = value;
}


int main()
{
  Circle circle;
  Circle.setRadius(10.0);
  cout << "반지름: " << Circle.getRadius() << endl;
  cout << "넓이: " << Circle.getArea() << endl;
  cout << "겉넓이: " << Circle.getSurface() << endl;
  cout << "부피: " << Circle.getVolume() << endl;
  return 0;
}
