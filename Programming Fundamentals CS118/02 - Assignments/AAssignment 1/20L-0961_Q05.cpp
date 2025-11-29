// Ammar Ahmed		20L-0961		Assignment 1, Question 5 //
#include <iostream>
using namespace std;

int main()
{

    int n, temp;
    cout << "Enter Number for  prime factorization ";
    cin >> n;
    temp = n;
    
    // If it is a factor of 2
    while (n % 2 == 0)
    {
        cout << 2 << " ";
        n /= 2;
    }

    // For factors 3 onwards, checking at odd intervals
    // we stop at n/2 for quicker calculations
    for (int i = 3; i <= n / 2; i += 2)
    {
        while (n % i == 0)
        {
            cout << i << " ";
            n /= i;
        }
    }

    if (n > 2)
        cout << n << " ";
    
    if(n==temp)
    {
        cout << endl;
        cout << " ," << temp << " is prime";
    }


    return 0;
}