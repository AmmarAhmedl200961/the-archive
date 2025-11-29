// Ammar Ahmed		20L-0961		Assignment 1, Question 2 //
#include <iostream>
#include <cmath>
using namespace std;

int main()
{

    // part a

    unsigned long long int n;

    cout << "Enter denary number: ";
    cin >> n;

    int r;
    unsigned long long int binary = 0, i = 1;

    while (n != 0) {
        r = n % 2;
        n /= 2;
        binary += (r * i);
        i *= 10;
    }
    cout << "Binary equivalent: " << binary;

    // part b

    cout << endl;


    unsigned long long int bin, dec = 0, j = 1, rem;
    cout << "Enter bin number: ";
    cin >> bin;
    while (bin != 0)
    {
        rem = bin % 10;
        dec += rem * j;
        j *= 2;
        bin /= 10;
    }
    cout << "Denary Equivalent: " << dec << "\n";
    

    return 0;
}