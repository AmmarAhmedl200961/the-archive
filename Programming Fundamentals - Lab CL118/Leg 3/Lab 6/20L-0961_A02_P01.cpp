#include <iostream>
using namespace std;

// Activity 02, Problem 01

int main()
{

    int n;

    cout << "n: ";
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
            cout << j;
        for (int k = i; k >= 1; k--)
            cout << k;
        cout << endl;
    }

    return 0;
}