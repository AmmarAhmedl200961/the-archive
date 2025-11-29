#include <iostream>
using namespace std;

// Question 3

int main()
{
	int v1, v2;
	char oper;

	cout << "Enter Number 1: ";
	cin >> v1;

	cout << "Enter Number 2: ";
	cin >> v2;

	cout << "Enter Operator: ";
	cin >> oper;

	if (oper == '+')
	{
		cout << v1 << oper << v2 << "=" << v1 + v2;
	}

	if (oper == '-')
	{
		cout << v1 << oper << v2 << "=" << v1 - v2;
	}

	if (oper == '*')
	{
		cout << v1 << oper << v2 << "=" << v1 * v2;
	}

	if (oper == '/')
	{
		cout << v1 << oper << v2 << "=" << v1 / v2;
	}

	return 0;
}