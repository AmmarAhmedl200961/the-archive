#include <iostream>
using namespace std;

int main()
{
    // Question 4

    int n, p;   // we will take p temporarily
    double sum = 0, average = 0;

    cout << "enter number to print average and sum of  ";
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cout << "enter number " << i + 1 << " ";
        cin >> p;
        sum += p;
    }

    average = sum / n;

    cout << "\nThe Sum of " << n << " numbers entered is " << sum << endl;
    cout << "\nThe Average of " << n << " numbers entered is " << average << endl;


    return 0;
}