#include <iostream>
using namespace std;

// Problem 4

int main()
{
	
	int in, counter = 1;
	cout << "Enter a number: ";
	cin >> in;

	cout << endl << "Table of " << in << endl;
	while (counter <= 10)
	{
		cout << in << " * " << counter << " = " << in * counter << endl;
		
		counter++;
	}

	return 0;
}