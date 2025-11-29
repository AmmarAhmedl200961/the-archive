#include <iostream>
#include <string.h>
using namespace std;

bool isSpacedPalindrome(string arr)
{
	int size = arr.length(); 
	int chk = -1;
	int start = 0, end = size - 2;
	while (start <= end)
	{
		if (arr[start] != arr[end])
		{
			chk++;
			return false;
			break;
		}
		end--;
		start++;
	}
	if (chk == -1)
	{
		return true;
	}
}


int main()
{
	cin.get();

	string arr;
	cin >> arr;
	
	if (isSpacedPalindrome(arr)==true)
	{
		cout << "is palindrome";
	}
	else
	{
		cout << "is not a palindrome";
	}



	return 0;
}