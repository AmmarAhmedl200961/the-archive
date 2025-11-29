#include <iostream>
using namespace std;

// Problem 5

int main()
{
	int arr[100];
	int size;
	cout << "enter your size of array 1\n";
	cin >> size;
	cout << "enter your array to find second largest (sorted)\n";
	
	for (int i = 0; i < size; i++)
	{
		cin >> arr[i];
	}

	max_minDiffer(arr, size);

	system("pause");
	return 0;
}

void max_minDiffer(int arr[], int size)
{
	int temp = 0, t, max, max1, min, min1;

	for (int i = 0; i < size; i++)
	{
		for (int j = 1; j < size; j++)
		{
			t = arr[i] - arr[j];

			if (t < 0)
			{
				t = t * (-1);
			}

			else if (temp < t)
			{
				temp = t;
				max = i;
				max1 = j;
			}
		}
	}

	cout << " Pair of elements with maximum difference: " << arr[max] << " " << arr[max1] << endl;

	for (int i = 0; i < size; i++)
	{
		for (int j = 1; j < size; j++)
		{
			t = arr[i] - arr[j];

			if (t < 0)
			{
				t = t * (-1);
			}

			else if (temp >= t)
			{
				temp = t;
				min = i;
				min1 = j;
			}
		}
	}

	cout << " Pair of elements with mainimum difference: " << arr[min] << " " << arr[min1] << endl;


}