#include <iostream> 
using namespace std; 

//void input()

void output(int arr[])
{
	for (int i = 0; i < 10; i++)
	{
		cout << arr[i] << " ";
	}
}

void sort(int arr[])
{
	int res[10];
	for (int i = 0; i < 10; i++)
	{
		if (arr[i] > arr[i + 1])
			res[i] = arr[i];
	}
	output(res);
}

int main()
{
	cin.get();

	int arr[10];
	for (int i = 0; i < 10; i++)
		arr[i] = -1;
	cout << "enter 10 values or -1 to stop ";
	int iter = 0;
	for (int i = 0; i < 10; i++)
	{
		iter = i;
		cin >> arr[i];
		if (arr[i] == -1)
			break;
		
	}

	cout << "your valid entries are " << iter;
	cout << "\nsorted array";

	sort(arr);

	return 0;
}