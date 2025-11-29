#include <iostream>
#include <cstring>
using namespace std;

//Question 1

int main()
{
	char arr[100], toReplace, toFind;

	cout << " Enter your string: ";
	cin.getline(arr, 100);

	cout << " Enter character to Find: ";
	cin >> toFind;

	cout << " Enter character to to Replace: ";
	cin >> toReplace;

	for (int i = 0; i < 100; i++)
	{
		if (arr[i] == toFind)
		{
			arr[i] = toReplace;
		}
	}

	cout << " New string is: ";

	for (int i = 0; i < 100; i++)
	{
		cout << arr[i];
	}

	cout << "\n";

	return 0;
}