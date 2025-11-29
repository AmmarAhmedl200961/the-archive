#include <iostream>
using namespace std;

// Question 2
// I had less idea of this part of the lab, i had to check online..

int main()
{
	int a[100], b[100], check = 0, n1, n2;
	cout << "array 1 size is  ";
	cin >> n1;
	cout << "\narray 2 size is  ";
	cin >> n2;
	cout << "\ninput array 1 elements...\n";
	for (int i = 0; i < n1; i++)
		cin >> a[i];
	cout << "\ninput array 2 elements...\n";
	for (int i = 0; i < n2; i++)
		cin >> b[i];
	cout << "\nintersection: ";
	for (int i = 0; i < n1; i++)
	{
		for (int j = 0; j < n2; j++)
		{
			if (b[i] == a[j])
				check = 1;	//	evaluates to intersectioned element
		}
		if (check == 1)
			cout << b[i];	//	will output intersectioned element.
		check = 0;
	}

	return 0;
}