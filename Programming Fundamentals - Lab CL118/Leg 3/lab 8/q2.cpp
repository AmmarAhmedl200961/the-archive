#include <iostream>
using namespace std;

// Problem 2

int main()
{
	int arr[11], count = 0, find, size = 11;
    
    cout << "input values ";

	for (int i = 0; i < size; i++)
	{
		cin >> arr[i];
	}

	cout << endl << "array has (";

	for (int i = 0; i < size; i++)
	{
		cout << arr[i] << " ";
	}

	cout << ")" << endl;
	cout << "Enter value to find occurence of ";
	cin >> find;


	for (int i = 0; i < size; i++)
	{
		if (arr[i] == find)
			count++;
	}

	cout << endl << find << " appeared " << count << " times";

    return 0;
}