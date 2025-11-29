#include <iostream>
using namespace std;

// Question 9

int main()
{
	float sales;

	cout << "Enter sales in rupees ";
	cin >> sales;

	if (sales < 0)
	{
		cout << "Sorry, salary cannot be calculated";
	}
	else
	{
		cout << "Salary is " << 2000 + (sales * 9 / 100);
	}
	
	return 0;
}