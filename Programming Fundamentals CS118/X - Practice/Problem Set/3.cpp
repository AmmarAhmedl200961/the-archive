#include <iostream>
using namespace std;

int main()
{
	cin.get();

	// code will work on a sorted array only

	int arr[10], count=0;

	cout << "enter element" << endl;


	for (int i = 0; i < 10; i++)
	{
		cin >> arr[i];
	}

	for (int i = 0; i < 10; i++)
	{
		
		for (int j = i + 1; j < 10; j++)	// k will check till i for unique elements
		{
			if (arr[i] == arr[j])
			{
				count++;
				continue;
			}
		}
	}

	cout << endl << "Count of duplicates found " << count;

	return 0;
}