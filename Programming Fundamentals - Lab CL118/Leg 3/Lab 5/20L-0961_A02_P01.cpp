#include <iostream>
using namespace std;

// Activity 2, Problem 1

int main()
{
	cin.get();

	int n, x = 0, y = 0, count=0;

	cout << "enter number of terms: ";

	cin >> n;

	for (n; n > 0; n -= 2)
	{
		x += 2;
		y += 5;

		if (count == 0)
			cout << x;

		else
			cout << " + " << x;

		if (n >= 1 || n == 0)
			cout << " - " << y;

		count++;
	}
	
	return 0;
}