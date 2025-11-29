#include <iostream>
using namespace std;

// Question 5

int main()
{
	int a, b, c;

	cout << "Enter Number1: ";
	cin >> a;

	cout << "Enter Number2: ";
	cin >> b;

	cout << "Enter Number3: ";
	cin >> c;

	if (a >= b)
	{
		if (a >= c)
		{
			if (b >= c)
			{
				cout << "Decreasing Order: " << a << " " << b << " " << c;
			}
			else
			{
				cout << "Decreasing Order: " << a << " " << c << " " << b;

			}
		}
		else
		{
			if (b >= c)
			{
				cout << "Decreasing Order: " << b << " " << c << " " << a;

			}
			else
			{
				cout << "Decreasing Order: " << c << " " << a << " " << b;

			}
		}

	}
	else
	{
		if (a >= c)
		{
			if (b >= c)
			{
				cout << "Decreasing Order: " << b << " " << a << " " << c;

			}
			else
			{
				cout << "Decreasing Order: " << c << " " << b << " " << a;

			}
		}
		else
		{
			if (b >= c)
			{
				cout << "Decreasing Order: " << b << " " << c << " " << a;

			}

			else
			{
				cout << "Decreasing Order: " << c << " " << b << " " << a;

			}
		}
	}


	return 0;
}