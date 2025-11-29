#include <iostream>
using namespace std;

// Problem 1

int main()
{
	int arr[] = { 0 };
	int size;
	cout << "enter your size of array 1\n";
	cin >> size;
	cout << "enter your array to find sum\n";
	
	for (int i = 0; i < size; i++)
	{
		cin >> arr[i];
	}

	cout << "sum of array is " << sumOfArray(arr, size);

	system("pause");
	return 0;
}

int sumOfArray(int arr[], int size)
{
	int sum = 0;

	for (int i = 0; i < size; i++)
		sum += arr[i];				// loop will go through each element and add to sum
	return sum;
}