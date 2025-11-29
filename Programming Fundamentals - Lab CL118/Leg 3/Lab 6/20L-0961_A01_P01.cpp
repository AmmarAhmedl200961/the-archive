#include <iostream>
using namespace std;

// Activity 01, Problem 01

int main()
{

    // Filled Square
    int H;

    cout << "H: ";
    cin >> H;

    for (int i = 1; i <= H; i++)
    {
        for (int j = 1; j <= H; j++)
        {
            cout << "*";
        }

        cout << endl;
    }

    // Hollow Square

    cout << "H: ";
    cin >> H;

    for (int i = 1; i <= H; i++)
    {
        for (int j = 1; j <= H; j++)
        {
            if (i == 1 || i == H ||
                j == 1 || j == H)
                cout << "*";
            else
                cout << " ";
        }
        cout << endl;
    }

    // Filled Triangle

    cout << "H: ";
    cin >> H;

    for (int i = 0; i < H; i++)
    {
        for (int j = 0; j < H; j++)
        {
            if (j < H - i - 1) 
                cout << " ";
            else 
                cout << "*";
        }
        cout << endl;
    }

    // Hollow Triangle

    cout << "H: ";
    cin >> H;

    for (int i = 1; i <= H; i++) {
        for (int j = i; j <= H; j++) {
            cout << " ";
        }
        for (int j = 1; j <= i; j++) {

            if (i == H || j == 1 || j == i) {
                cout << "*";
            }
            else {
                cout << " ";
            }
        }
        cout << endl;
    }


    return 0;
}