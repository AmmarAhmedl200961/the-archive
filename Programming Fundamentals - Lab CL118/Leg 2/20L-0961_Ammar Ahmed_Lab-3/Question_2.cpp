#include <iostream>

using namespace std;

int main()
{
    // Question 2

    int n, index = 1;

    cout << "enter number to print numbers of  ";
    cin >> n;

    while (index <= n)     //condition will stop exactly at n
    {
        cout << index << endl;
        index++;
    }

    return 0;
}