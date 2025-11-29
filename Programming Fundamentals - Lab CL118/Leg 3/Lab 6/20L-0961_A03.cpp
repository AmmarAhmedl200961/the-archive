#include <iostream>
using namespace std;

// Activity 03

int main()
{

    int num, count, rem;
    cout << "Enter a number: ";
    cin >> num;
    for (int chk = 0; chk < 10; chk++)
    {
        cout << "Frequency of " << chk << "= ";
        count = 0;
        for (int j = num; j > 0; j = j / 10)
        {
            rem = j % 10;
            if (rem == chk)
            {
                count++;
            }
        }
        cout << count << endl;
    }

    return 0;
}