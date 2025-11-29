// Ammar Ahmed		20L-0961		Assignment 1, Question 1 //
#include <iostream>
using namespace std;

int main()
{

    // part a

    double terms, sign = 1;
    cout << "Enter value of terms to evaluate ";
    cin >> terms;

    if (terms > 0) 
    {
        double pi = 0.0;
        for (int i = 0; i < terms; i++) 
        {
            pi += sign / (2.0 * i + 1.0);
            sign = -sign;
        }
        // Since pi will be pi/4 here
        pi *= 4;
        cout << "Value of pi: " << pi;
    }
    else {
        cout << "Wrong value of terms entered";
    }

    cout << endl;

    // part b

    int x, num;
    cout << "Enter x: ";
    cin >> x;
    cout << "Enter number of terms to evaluate: ";
    cin >> num;

    float sum = 1.0; 

    for (int i = num - 1; i > 0; i--)
        sum = 1 + x * sum / i;
    cout << sum;

    return 0;
}