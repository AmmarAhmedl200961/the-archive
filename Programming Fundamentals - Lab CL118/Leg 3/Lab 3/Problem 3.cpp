#include <iostream>
using namespace std;

// Problem 3 

int main()
{
	
	int i, in, counter = 0;
	cout << "Enter a number: ";
	cin >> in;
	i = in;
	while (counter < 10)
	{
		cout << i * i << " ";
		i++, counter++;
	}

	return 0;
}