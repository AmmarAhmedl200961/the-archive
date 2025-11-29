#include <iostream>
using namespace std;

int main()
{
    int x;
    cout << "enter number\n";
    cin >> x;       // x=15
/*
    if (x <= 0)
        cout << "invalid number\n";
    else if (x == 1)
        cout << "neither prime nor composite\n";
    else if (x == 2)
        cout << "number is prime";
    else
    {*/
        int flag = 0;       // flag shows number is composite

        for (int i = 1; i < x ; i++)    // here && was flag != -1, to break loop
        {
            if (x % i == 0)
                cout << i << " ";
        }
        cout << x;


        /*if (flag == 1)
            cout << "composite number\n";
        else
            cout << "prime number\n";
            */
    





    cin.get();

    return 0;
}