#include <iostream>
using namespace std;

// Question 02

int main()
{
    float num, sum = 0, sign = -1;
    cout << "Log 2 of: ";
    cin >> num;

    for (float i = 1; i <= num; i++)
    {
        int counter = 1;
        
        sign *= -1;
        sum += sign * 1.0 / i;
        
        if (counter == 1)
        {
            cout << "1";
        }
        else
        {
            cout << (float)sign * 1.0 / i;
        }
        counter++;
    }

    cout << "=" << sum;

    return 0;
}