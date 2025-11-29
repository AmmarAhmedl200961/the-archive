#include <iostream>
using namespace std;

// Question 4

int main()
{
	int a, b, c;

	cout << "Enter Number1: ";
	cin >> a;

	cout << "Enter Number2: ";
	cin >> b;

	cout << "Enter Number3: ";
	cin >> c;

	if (a < c)
	{

		if (a < b)
		{
			cout << "Smallest Number " << a;
		}
		else
			cout << "Smallest Number " << b;
	}

	else
	{
		if	(b < c)
		{
			cout << "Smallest Number " << b;
		}
		
		else
		{
			cout << "Smallest Number " << c;
		}
	}
	


	return 0;
}