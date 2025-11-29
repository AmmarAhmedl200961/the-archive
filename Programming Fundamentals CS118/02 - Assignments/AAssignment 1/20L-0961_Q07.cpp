// Ammar Ahmed		20L-0961		Assignment 1, Question 7 //
#include <iostream>
using namespace std;

int main()
{
	int x1, y1, x2, y2;

	cout << " Enter 1st coordinate: ";
	cin >> x1 >> y1;

	cout << " Enter 2nd coordinate: ";
	cin >> x2 >> y2;

	int grad = (y2 - y1) / (x2 - x1);
	int c = y1 - (grad * x1);

	cout << " Approximate linear equation: ";
	cout << " y = " << grad << "x";

	if (c >= 0)
	{
		cout << " + " << c << endl;
	}

	else
	{
		cout << " " << c << endl;
	}

	cout << endl << endl;

	int max;
	int ny1 = y1;
	int ny2 = y2;

	if (y1 < 0)
	{
		ny1 = y1 * -1;
	}

	if (y2 < 0)
	{
		ny2 = y2 * -1;
	}

	if (y1 > y2)
	{
		max = ny1;
	}

	else
	{
		max = ny2;
	}

	int n=0;

	for (int i = max*2; i >= 0; i--)
	{
		for (int j = max*2; j >= 0; j--)
		{
			if (j == n)
			{
				cout << " X ";
			}

			else if (j == max)
			{
				cout << " | ";
			}

			else if (i == max)
			{
				cout << " - ";

			}

			else
			{
				cout << "   ";
			}

		}

		n++;
		cout << endl;
	}

	cout << endl << endl;

	return 0;
}