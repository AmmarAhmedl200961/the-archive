#include <iostream>
using namespace std;

// Problem 1

struct Date
{
    int day;
    int month;
    int year;

};

int main()
{
    

    struct Date First, Second;

    cout << "Enter day, month and year respectively\n";

    cout << "Enter First date\n";
    cin >> First.day >> First.month >> First.year;
    cout << "Enter Second date\n";
    cin >> First.day >> First.month >> First.year;

    if ((First.day == Second.day) && (First.month == Second.month) && (First.year == Second.year))
        cout << "\"Dates are equal\"";
    else
        cout << "\"Dates are not equal\"";

    return 0;
}