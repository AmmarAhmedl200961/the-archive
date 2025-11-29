#include <iostream>
using namespace std;

// Problem 1

bool inPal(int x)
{
    int pal = 0, temp = 0;
    temp = x;

    while (x > 0)
    {
        pal = pal * 10 + x % 10;
        x /= 10;
    }

    if (pal == temp)
    {
        return true;
    }

    else
    {
        return false;
    }
}

int main()
{
    int num;
    cout << "Enter number ";
    cin >> num;

    if (inPal(num))
    {
        cout << num << " is palindrome";
    }

    else
    {
        cout << num << " is not a palindrome";
    }

	return 0;
}