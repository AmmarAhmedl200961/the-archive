#include <iostream>
using namespace std;

int main()
{
	cin.get();

	// code will work on a sorted array only

	int arr[10];

	cout << "enter element" << endl;


	for (int i = 0; i < 10; i++)
	{
		cin >> arr[i];
	}

	for (int i = 0; i < 10; i++)
	{
		int k;
		for (k = 0; k < i; k++)	// k will check till i for unique elements
			if (arr[i] == arr[k])
				break;
		if (i == k)
			cout << arr[i] << " ";
	}

	return 0;
}