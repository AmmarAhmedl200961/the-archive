#include <iostream>
#include <cstring>
using namespace std;

int main()
{
	cin.get();

	char arr[] = "ABBA";

	int sz = sizeof(arr) / sizeof(arr[0]);
	
	int chk = -1;
	int si = 0, ei = sz - 2;
	
	while (si <= ei)
	{
		if (arr[si] != arr[ei])
		{
			chk++;
			cout << "Not Palindrome " << endl;
			break;
		}
		ei--;
		si++;
	}
	if (chk == -1)
	{
		cout << "Palindrome\n";
	}
	return 0;
}