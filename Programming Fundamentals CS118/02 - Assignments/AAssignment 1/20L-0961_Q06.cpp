// Ammar Ahmed		20L-0961		Assignment 1, Question 6 //
#include <iostream>
using namespace std;

int main()
{
    // part a

    int f;
    cout << "Enter height: ";
    cin >> f;

    for (int i = 0; i < f; i++)
    {
        for (int sp = i; sp < f; sp++)
        {
            cout << " ";
        }
        for (int st = 0; st <= (2 * i); st++)
        {
            cout << "*";
        }
        cout << endl;
    }

    cout << endl;
    // part b

    int d;
    cout << "Enter height: ";
    cin >> d;

    for (int i = 1; i <= d; i++)
    {
        for (int sp = i; sp < d; sp++)
        {
            cout << " ";
        }
        for (int st = 1; st <= (2 * i - 1); st++)
        {
            cout << "*";
        }
        cout << endl;
    }
    for (int i = d; i >= 1; i--)
    {
        for (int sp = i; sp <= d; sp++)
        {
            cout << " ";
        }
        for (int st = 2; st < (2 * i - 1); st++)
        {
            cout << "*";
        }
        cout << endl;
    }

    cout << endl;
    // part c

    int h;
    cout << "Enter height: ";
    cin >> h;

    for (int i = 1; i <= h; i++)
    {
        for (int j = i; j < h; j++)
        {
            cout << " ";
        }
        for (int j = 1; j <= (2 * i - 1); j++)
        {
            if (i == h || j == 1 || j == (2 * i - 1))
            {
                cout << "*";
            }
            else
            {
                cout << " ";
            }
        }

        cout << endl;
    }

    return 0;
}