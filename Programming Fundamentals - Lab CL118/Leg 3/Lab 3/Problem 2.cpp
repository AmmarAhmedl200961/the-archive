#include <iostream>
using namespace std;

// Problem 2

int main()
{

	int i = 0, sum = 0;

	cout << "Enter a number: ";
	cin >> i;

	while (!(i < 0))
	{
		sum += i;
		cout << "Enter a number: ";
		cin >> i;
	}

	cout << endl;

	cout << "The sum is " << sum;

	return 0;
}