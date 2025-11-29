#include <iostream>
using namespace std;

// Problem 6

int main()
{
    int in, f=1;
    cout << "Enter a positive integer: ";
    cin >> in;
    
    int i = 1;

    while (i <= in)
    {
        f *= i;
        i++;

    }

    cout << "Factorial of " << in << " = " << f;

    return 0;
}