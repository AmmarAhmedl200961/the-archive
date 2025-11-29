#include <iostream>
using namespace std;

// Question 8

int main()
{
	float pay, h;

	cout << "Enter hours worked ";
	cin >> h;

	cout << "Enter the hourly rate of the employee (Rs.): ";
	cin >> pay;

	if (h <= 40)
	{
		cout << "Salary is Rs. " << h * pay;
	}
	else
	{
		float straight = 40 * pay;
		float timeAndHalf = ((h - 40) * pay) + ((h - 40) / 2 * pay);
		cout << "Salary is Rs. " << straight + timeAndHalf;
	}


	return 0;
}