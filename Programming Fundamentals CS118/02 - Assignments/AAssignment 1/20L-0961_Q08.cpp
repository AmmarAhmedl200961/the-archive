// Ammar Ahmed		20L-0961		Assignment 1, Question 8 //
#include <iostream>
using namespace std;

int main()
{
    double n;
    cout << "Find special numbers in interval: ";
    cin >> n;

    for (double i = 0; i < n; i++)
    {
        double s = 0, count = 0;
        int r, comp; // we cannit double these variables


        comp = i;
        while (comp != 0)
        {
            comp /= 10;
            count++;
            // count will return number of digits 
        }

        comp = i;
        while (comp != 0)
        {
            int pow = 1;
            r = comp % 10; 

            for (int i = 1; i <= count; i++) // This loop will find power of number correlated to digit count
                pow *= r;

            s += pow; 
            comp /= 10;
        }
        if (i == s)
            cout << i << " ";
    }

    return 0;
}
