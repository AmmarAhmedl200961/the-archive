#include <iostream>
using namespace std;

// Problem 3

void displayseries(int starting_num, int rows)
{

    for (int i = rows; i >= 1; i--)
    {
        for (int j = 1; j <= i; j++)
        {
            if (starting_num == 10)
                starting_num = 0;
            cout << starting_num++ << "*";
        }
        cout << endl;
    }
}

int main()
{
    int a, b;
    cout << "Enter starting num and number of rows for series";
    cin >> a >> b;

    displayseries(a, b);

	return 0;
}