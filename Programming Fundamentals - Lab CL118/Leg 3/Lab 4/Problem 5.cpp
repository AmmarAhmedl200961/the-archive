#include <iostream>
using namespace std;

// Problem 5

int main() 
{
	int num;
	cout << "Input a number ";
	cin >> num;

	for (int i = 1; i <= num; i++)
	{
		if (num % i == 0)
		{
			cout << i << ",";
		}
	}
	
	return 0;
}