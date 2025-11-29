#include <iostream>
using namespace std;

// Activity 02, Problem 02

int main()
{

	int out, in;

	cout << "Enter outer loop: ";
	cin >> out;

	cout << "Enter inner loop: ";
	cin >> in;

	for (int i = 0; i < out; i++)
	{
		int a = in;
		int n2 = 1;

		for (int j = 0; j < in; j++)
		{
			cout << a;
			a--;

			cout << n2++;
		}

		cout << endl;
	}


    return 0;
}