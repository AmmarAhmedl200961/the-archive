#include <iostream>
using namespace std;

// Problem 4

int main() 
{
    int num, x = 0, y = 0;
    cout << "Enter a number for equation (1 + 2 + ... + n)^2 – (1^2 + 2^2 + ... + n^2 ) ";
    cin >> num;

    for (int i = 1; i <= num; i++)
    {
        x += i;
        y += (i * i);
    }

    cout << x * x << "-" << y <<" = "<< x * x - y;
    
    return 0;
}