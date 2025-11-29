#include <iostream>
using namespace std;

int main()
{
	cin.get();

	float a1, a2, a3;
	
	cout << "enter angles" << endl;
	
	cin >> a1 >> a2 >> a3;

	cout << "\ncalculating" << endl;
	if ((a1 > 0 && a2 > 0 && a3 > 0) && (a1 + a2 + a3) == 180)
	{
		cout << "\nangle entered correctly";
	}

	else
	{
		cout << "wrong angle input, angles do not add up to 180";

	}

	return 0;
}