#include <iostream>
using namespace std;

int main
{
	// Question 6

    int year;
    cout << "Enter your year ";
    cin >> year;

    // Leap year check

    if ((year % 400 == 0)                       // checks for century leap year
        || year % 4 == 0 && year % 100 != 0)    // checks for non century leap year 
        cout << "January\t days 31\nFebruary\t days 29\nMarch\t days 31\nApril\t days 30\nMay \t days 31\nJune\t days 30\nJuly\t days 31\nAugust\t days 31\nSeptember\t days 30\nOctober\t days 31\nNovember\t days 30\nDecember\t days 31";
    else
        cout << "January\t days 31\nFebruary\t days 28\nMarch\t days 31\nApril\t days 30\nMay \t days 31\nJune\t days 30\nJuly\t days 31\nAugust\t days 31\nSeptember\t days 30\nOctober\t days 31\nNovember\t days 30\nDecember\t days 31";
        
	return 0;
}
	