#include <iostream>
using namespace std;

// Activity 2, Problem 2

int main()
{
    //  basic fibonacci series
    //  0, 1, 1, 2, 3, 5, 8, 13, 21, ...

    int num, first = 0, second = 1, next = 0;

    cout << "Terms: ";
    cin >> num;

    for (int i = 0; i <= num; i++) 
    {
        if (i == 0) 
        {
            cout << first << ", ";
            continue;
            // executes above statement and progresses loop
        }
        if (i == 1) 
        {
            cout << second << ", ";
            continue;
            // executes above statement and progresses loop
        }
        next = first + second;
        first = second;
        second = next;

        cout << next << ", ";
    }
	
    return 0;
}