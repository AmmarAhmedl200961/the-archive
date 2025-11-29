#include <iostream>
using namespace std;

int main
{
	// Question 5

    char op;
    int v1, v2;

    cout << "Enter two integer numbers: ";
    
    cin >> v1 >> v2;

    cout << "\nEnter operator to use on integers, either + or - or * or % or / or P(POWER) or S(Square root of both numbers) ";
    cin >> op;

    switch (op)
    {
    case '+':
        cout << v1 + v2;
        break;

    case '-':
        cout << v1 - v2;
        break;

    case '*':
        cout << v1 * v2;
        break;

    case '%':
        cout << v1 % v2;
        break;

    case '/':
        if (v2 == 0)
        {
            cout << "Division not possible by 0";
            break;
        }
        else
        {
            cout << (float)(v1 / v2);
            break;
        }

    case 'P':
        cout << pow(v1, v2);
        break;

    case 'S':
        cout << "square root of first variable " << sqrt(v1) << endl;
        cout << "square root of second variable " << sqrt(v2) << endl;

    default:
        cout << "Error! operator is not correct";
        break;
    }
    
	return 0;
}
	