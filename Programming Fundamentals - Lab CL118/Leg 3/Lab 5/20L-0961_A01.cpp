#include <iostream>
using namespace std;

// Activity 1

int main()
{
	cin.get();

	// Spaces and Asterisk printing

	int sp, ast;

	cout << "Enter Spaces to output ";
	cin >> sp;

	for (int i = 0; i < sp; i++)
	{
		cout << " ";
	}

	cout << endl << "Enter Asterisk to output ";
	cin >> ast;

	for (int j = 0; j < ast; j++)
	{
		cout << "* ";
	}

	// Filled square

	int h, count = 0;

	cout << "Filled Square of Height H: ";

	cin >> h;

	for (int i = 0; i < h * h; i++)
	{
		cout << "*";
		count++;

		if (count == h)
		{
			cout << endl; 
			count = 0;
		}
	}

	// Hollow square

	// Filled Right triangle

	cout << "Filled Right triangle of Height H: ";
	cin >> h;

	for (int i = 0; i < h * h; i++)
	{

	}

	
	return 0;
}