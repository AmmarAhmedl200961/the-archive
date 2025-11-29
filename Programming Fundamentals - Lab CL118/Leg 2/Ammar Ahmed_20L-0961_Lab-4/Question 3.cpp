#include <iostream>
using namespace std;

// Question 3
// I had less idea of this part of the lab, i had to check online..


int main()
{
	string arr[30] = {"Welcome to character arrays"};
	cout << "enter a sentence of 30 words to flip\n";

	for (int i = 0; i < 30; i++)
		cin >> arr[i];
	
	int n = sizeof(arr) / sizeof(arr[0]);
	
	//	to print entered array
	for (int i = 0; i < n; i++)
		cout << arr[i] << " ";
	cout << endl;
	
	//	to reverse printed array
	int start = 0, end = n - 1;
	while (start < end)
	{
		string temp = arr[start];
		arr[start] = arr[end];
		arr[end] = temp;
		start++;
		end--;
	}
	
	//	to print reversed array
	for (int i = 0; i < n; i++)
		cout << arr[i] << " ";
	cout << endl;

	return 0;
}