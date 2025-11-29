#include <iostream>
using namespace std;

// Problem 3

int main() 
{
    int num, sum = 0;
    cout << "Enter a number to print squares up to ";
    cin >> num;

    for (int i = 1; i <= num; i++)
    {
        int temp;
        temp = i * i;
        cout << temp << ",";
        sum += temp;
    }

    cout << "Avg=" << sum / num;


    return 0;
}