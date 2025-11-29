#include <iostream>
using namespace std;

// Question 3a

int main()
{
	int r, c, temp;
	int arr[10][10];

	cout << " Enter number of rows: ";
	cin >> r;

	cout << " Enter number of columns: ";
	cin >> c;

	cout << " Enter array: ";

	for (int i = 0; i < r; i++)
	{
		for (int j = 0; j < c; j++)
			cin >> arr[i][j];
		
	}

	cout << " Array entered is: " << endl;
	// Array Display
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


	for (int i = 0; i < r; i++)
	{
		for (int j = 0; j < c / 2; j++)
		{
			temp = arr[i][j];
			arr[i][j] = arr[i][(c - 1) - j];
			arr[i][(c - 1) - j] = temp;
		}
	}

	cout << " Array after flip is: " << endl;
	// Vertical flips
	for (int i = 0; i < r; i++)
	{
		for (int j = 0; j < c; j++)
		{
			cout << arr[i][j] << " ";

			if (j == c - 1)
				cout << endl;
			
		}
	}

	system("pause");
	return 0;
}