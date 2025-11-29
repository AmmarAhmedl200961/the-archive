#include <iostream>
#include <cstring>
using namespace std;

int main()
{
	cin.get();

	char arr[] = "My Name is Ammar Ahmed";
	char sub[] = "is";
	int si;
	int chk = -1;
	for (int i = 0; arr[i] != '\0'; i++)
	{
		if (arr[i] == sub[0])
		{
			chk = -1;
			si = i;
			for (int j = 0; sub[j] != '\0'; j++)
			{
				if (sub[j] != arr[si])
				{
					chk++;
					break;
				}
				si++;
			}
			if (chk == -1)
			{
				cout << "Founded at " << i << endl;
			}
		}

	}

	return 0;
}