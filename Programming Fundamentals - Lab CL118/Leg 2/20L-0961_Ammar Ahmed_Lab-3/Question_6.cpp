#include <iostream>
using namespace std;

int main()
{
    // Question 5

    int n, factorial, sign = -1;    // as we will be alternating the sign
    float x, y, sum = 0;

    cout << "enter the value of x: ";
    cin >> x;
    cout << "enter the value of n: ";
    cin >> n;

    for (int i = 1; i <= n; i += 2)
    {
        y = 1;
        factorial = 1;
        
        for (int j = 1; j <= 1; j++)
        {
            y = y * x;
            factorial = factorial * j;

        }
        sign = -1 * sign;
        sum += sign * y / factorial;
    }

    cout << "sin " << x << " = " << sum;

    // i had to search online for a better explanation

    return 0;
}