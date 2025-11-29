#include <iostream>
using namespace std;

// Question 7

int main()
{
	int a, b, c;

	cout << "Enter Number1: ";
	cin >> a;

	cout << "Enter Number2: ";
	cin >> b;

	cout << "Enter Number3: ";
	cin >> c;

	if (a < b && b < c)
	{
		cout << "Ascending Order: " << a << " " << b << " " << c;

	}
	else if (b < a && a < c)
	{
		cout << "Ascending Order: " << b << " " << a << " " << c;

	}
	else if (c < b && b < a)
	{
		cout << "Ascending Order: " << c << " " << b << " " << a;

	}
	else if (c < a && a < b)
	{
		cout << "Ascending Order: " << c << " " << a << " " << b;

	}
	else if (b < c && c < a)
	{
		cout << "Ascending Order: " << b << " " << c << " " << a;

	}
	else if (a < c && c < b)
	{
		cout << "Ascending Order: " << a << " " << c << " " << b;

	}


	return 0;
}