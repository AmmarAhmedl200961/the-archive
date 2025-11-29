#include <iostream>
using namespace std;

// Question 1

int main()
{
	int r, c;
	int arr[50][50];

	cout << " Enter number of rows: ";
	cin >> r;

	cout << " Enter number of columns: ";
	cin >> c;

	cout << " Enter array: ";

	// Array Input
	for (int i = 0; i < r; i++)
	{
		for (int j = 0; j < c; j++)
		{
			cin >> arr[i][j];

			while (arr[i][j] > 9)	// total elements should be less than 10, then this loop will trigger
			{
				cout << " value should be less than 10 " << endl;
				cin >> arr[i][j];
			}
		}
	}

	// Array Printing
	cout << " Array entered is: " << endl;
	for (int i = 0; i < r; i++)
	{
		for (int j = 0; j < c; j++)
		{
			cout << arr[i][j] << " ";

			if (j == c - 1)
			{
				cout << endl;
			}
		}
	}

	system("pause");
	return 0;
}