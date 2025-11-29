#include <iostream>
using namespace std;

// Question 6

int main()
{
	int a, b, c;

	cout << "Enter Number1: ";
	cin >> a;

	cout << "Enter Number2: ";
	cin >> b;

	cout << "Enter Number3: ";
	cin >> c;

	if (a > b && a > c)
	{
		cout << "Largest Number " << a;
	}
	else if (b > a && b > c)
	{
		cout << "Largest Number " << b;
	}
	else if (c > a && c > b)
	{
		cout << "Largest Number " << c;
	}

	return 0;
}