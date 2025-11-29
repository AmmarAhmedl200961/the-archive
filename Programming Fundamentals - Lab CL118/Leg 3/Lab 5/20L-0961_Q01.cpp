#include <iostream>
using namespace std;

// Question 01

int main()
{
    int n, sum = 0;

    for(;;)
    {
        cout << "Enter Number: ";
        cin >> n;

        if (n != 101)
            sum += n;
        else
            break;
    }

    cout << "Sum: " << sum;

    return 0;
}