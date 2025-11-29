#include <iostream>
using namespace std;

struct Date
{
	int dd;
	string mm;
	int yyyy;
};

int main()
{
	Date d, d2;

	cout << "Enter dd-mm-yyyy 1\n";
	cin >> d.dd >> d.mm >> d.yyyy;

	cout << "Enter dd-mm-yyyy 2\n";
	cin >> d2.dd >> d2.mm >> d2.yyyy;

	if (d.dd == d2.dd && d.mm == d2.mm && d.yyyy == d2.yyyy)
		cout << "dates are equal";
	else
		cout << "dates are not equal";

	return 0;
}