// Ammar Ahmed		20L-0961		Assignment 1, Question 3 //
#include <iostream>
using namespace std;

int main()
{

    // part a

    int n;
    cout << "Enter n: ";
    cin >> n;
    int r = 0;

    while (n > 0)
    {
        r = r * 10 + n % 10;
        n /= 10;
    }

    cout << "reverse: " << r;

    // part b

    int chk, pal = 0, temp = 0;
    cout << "Enter n: ";
    cin >> chk;
    temp = chk;

    while (chk > 0)
    {
        pal = pal * 10 + chk % 10;
        chk /= 10;
    }

    if (pal == temp)
    {
        cout << endl << "palindrome";
    }

    else 
    {
        cout << endl << "not a palindrome";
    }
    
    return 0;
}