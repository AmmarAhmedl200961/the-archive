#include <iostream>
using namespace std;

// Problem 5

int main()
{
    int in, counter = 1, flag = 0;
    cout << "Enter Number: ";
    cin >> in;

    while (counter <= in)
    {
        if (in % counter == 0)
            flag++;
        counter++;
    }
    if (flag == 2)
        cout << endl << "Number is Prime";
    else
        cout << endl << "Number is not Prime";
    
    return 0;
}