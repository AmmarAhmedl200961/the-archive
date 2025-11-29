#include <iostream>
using namespace std;

// Problem 1

int main()
{
	int arr[5], small, big;

	cout << "array has ";
	for (int i = 0; i < 5; i++)
	{
		cout << arr[i] << " ";
	}

	cout << endl;
    cout << "input values ";

	for (int i = 0; i < 5; i++)
	{
		cin >> arr[i];
	}

    big = arr[0];

    for (int i = 0; i < 5; i++)
    {
        if (big < arr[i])   
        {
            big = arr[i]; 
        }
    }
    cout << "Largest value of array " << big << endl;

    small = arr[0];   // initializing

    for (int i = 0; i < 5; i++)
    {
        if (small > arr[i])   
        {
            small = arr[i];   
        }
    }
    cout << "Smallest value of array " << small;


	return 0;
}