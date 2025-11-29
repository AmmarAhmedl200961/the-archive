#include <iostream>
using namespace std;

int main()
{
    // Question 5

    int n = 0, counter = 0, max = 0;
    double sum = 0, average = 0;
    int min = max;

    cout << "enter your numbers to find max-min and sum-average of till -1 ";
    
    max = min = num;    // all should be equal 

    do
    {
        cin >> n;
        if (n != -1)
        {
            ++counter;
            sum += n;
            if (max < n)
                max = n;
            if (min > n)
                min = n;
        }

        else
            cout << "\n\nterminating.." << endl;

    }     while (!(n = -1));


    average = sum / n;

    cout << "\nThe Sum is "  << sum << endl;
    cout << "\nThe Average is " << average << endl;
    cout << "\nThe Max is " << max << endl;
    cout << "\nThe Min is " << min << endl;
    
    /* I could not understand most of this question so output may differ
    please explain if you have time.*/
    
    return 0;
}