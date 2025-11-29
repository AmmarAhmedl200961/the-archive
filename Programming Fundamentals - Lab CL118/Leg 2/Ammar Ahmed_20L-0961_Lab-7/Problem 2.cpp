#include <iostream>
using namespace std;

// Problem 2

int main()
{
	int arr[100];
	int size;
	cout << " Enter number of elements: ";
	cin >> size;

	cout << " Enter Array: ";

	for (int i = 0; i < size; i++)
	{
		cin >> arr[i];
	}

	cout << "second largest element is " << secondLargesteElement(arr, size);

	system("pause");
	return 0;
}

int secondLargesteElement(int arr[], int size)
{
	int last, second;

	if (arr[0] < arr[1])
	{
		last = arr[1];
		second = arr[0];
	}

	else
	{
		last = arr[0];
		second = arr[1];
	}

	for (int i = 2; i < size; i++)
	{
		if (arr[i] > last)
		{
			second = last;
			last = arr[i];
		}

		else if (arr[i] > second && arr[i] != last)
		{
			second = arr[i];
		}
	}

	return second;
}