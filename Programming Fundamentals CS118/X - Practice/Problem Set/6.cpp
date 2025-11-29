#include <iostream>
using namespace std;

int main()
{
	cin.get();

	int sum = 0, n;

	cout << "enter numbers to find sum of ";

	cin >> n;

	while (n > 0)
	{
		sum += n % 10;
		n /= 10;
	}

	cout << "\nSum is " << sum;

	return 0;
}