#include <iostream>
using namespace std;

// Question 2

int main()
{
	float grade;

	cout << "Enter Score: ";

	cin >> grade;

	if (grade < 50)
	{
		cout << "Your Grade: F";
	}

	else if (grade >= 50 && grade <= 59)
	{
		cout << "Your Grade: D";

	}

	else if (grade >= 60 && grade <= 69)
	{
		cout << "Your Grade: C";

	}

	else if (grade >= 70 && grade <= 79)
	{
		cout << "Your Grade: B";

	}

	else if (grade >= 80 && grade <= 89)
	{
		cout << "Your Grade: A";

	}

	else if (grade >=90)
	{
		cout << "Your Grade: D";

	}

	return 0;
}