#include <iostream>
using namespace std;

// Problem 1

int main() 
{
    int num, sum=0;

    cout << "Enter a number to print to ";
    cin >> num;

    for (int i = 1; i <= num; i++)
    {
        if (i % 2 != 0)
        {
            cout << i << " ";
            sum += i;
        }
    }

    cout << endl << "Sum: " << sum;
    
    return 0;
}