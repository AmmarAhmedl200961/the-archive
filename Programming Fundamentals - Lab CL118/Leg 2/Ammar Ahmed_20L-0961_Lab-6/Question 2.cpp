#include <iostream>
using namespace std;

// Question 2

int main()
{
	int r, c, sum = 0;
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

			// Diagonal Sum procedure
			if (i == j) 
			{
				sum += arr[i][j];
			}
		}
	}

	cout << " Array entered is: " << endl;
	// Array Output
	for (int i = 0; i < r; i++)
	{
		for (int j = 0; j < c; j++)
		{
			cout << arr[i][j] << " ";

			if (j == c - 1)
				cout << endl;
			
		}
	}

	cout << " Trace: " << sum << endl;

	system("pause");
	return 0;
}