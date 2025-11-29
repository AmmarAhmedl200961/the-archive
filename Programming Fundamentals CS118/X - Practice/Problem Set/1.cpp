#include <iostream>
using namespace std;

int main()
{
	cin.get();

	// code will work on a sorted array only

	int arr[10], count;
	
	cout << "enter element" << endl;

	for (int i = 0; i < 10; i++)
	{
		cin >> arr[i];
	}

	for (int i = 0; i < 10; i++)
	{
		int count = 0;

		for (int j = 1; j < 10; j++)
		{
			if (arr[j] == -1)
				i++;
			
			else if (arr[i] == arr[j])
			{
				count++;
				arr[j] = -1
			}
			
		}
		cout << arr[i] << "\t" << count << endl;

	}

	return 0;
}