#include <iostream>
using namespace std;

int main()
{
    // Question 3

    int n;

    cout << "enter number to print squares of  ";
    cin >> n;

    for (int i = 1; i <= n; ++i)
    {
        cout << pow(i, 2) << endl;
    }

    return 0;
}