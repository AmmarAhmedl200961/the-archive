#include <iostream>
using namespace std;

// Problem 3

int main()
{
	int arr1[100], arr2[100], sizeOfarray1, sizeOfarray2;

	cout << " Enter size of array 1: ";
	cin >> sizeOfarray1;

	cout << " Enter size of array 2: ";
	cin >> sizeOfarray2;

	cout << " Enter array 1: ";

	for (int i = 0; i < sizeOfarray1; i++)
	{
		cin >> arr1[i];
	}

	cout << " Enter array 2: ";

	for (int i = 0; i < sizeOfarray1; i++)
	{
		cin >> arr2[i];
	}

	printUniqueElementArray(arr1, arr2, sizeOfarray1, sizeOfarray2);

	system("pause");
	return 0;
}

void printUniqueElementArray(int arr1[], int arr2[], int sizeOfarray1, int sizeOfarray2)
{
	for (int i = 0; i < sizeOfarray1; i++)
	{
		for (int j = 0; j < sizeOfarray2; j++)
		{
			if (arr1[i] == (arr2[j]))
				cout << "common element is" << arr1[i];
		}
	}
}
