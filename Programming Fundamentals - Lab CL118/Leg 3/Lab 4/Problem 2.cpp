#include <iostream>
using namespace std;

// Problem 2

int main() 
{
    int num, times;

    cout << "Number to multiply AND times ";
    cin >> num >> times;


    if (times > 1)
    {
        int product = 0;

        for (int i = 1; i <= times; i++)
        {
            product+=num;
        }
        cout << product;
    }
    else
    {
        cout << num;
    }

    return 0;
}