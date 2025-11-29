#include <iostream>
using namespace std;

int main
{
	 // Question 8

    int num;
    cout << "Enter number to find factorial of (ranging from 1-10) ";
    cin >> num;

    switch (num)
    {
    case 1:
        cout << "1";
        break;

    case 2:
        cout << "2";
        break;

    case 3:
        cout << "6";
        break;

    case 4:
        cout << "24";
        break;

    case 5:
        cout << "120";
        break;

    case 6:
        cout << "720";
        break;

    case 7:
        cout << "5040";
        break;

    case 8:
        cout << "40320";
        break;

    case 9:
        cout << "362880";
        break;

    case 10:
        cout << "3628800";
        break;

    default:
		cout<<"Not in specified range !!!";
        break;
    }

	return 0;
}
	