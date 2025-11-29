#include <iostream>
#include <cstring>
using namespace std;

int main()
{
	char str[100];
	char tempWord[30];
	int a = 0, k = 0, j = 0;

	cout << " Enter your string: ";
	cin.getline(str, 100);

	cout << " New array is: " << endl;

	for (int i = 0; i < 100; i++)
	{
		while (j < 100)
		{
			if (str[a] != ' ')
			{
				tempWord[a] = str[a];
				a++;
			}

			if (str[a] == ' ')
			{
				tempWord[a] = '\0';
				a++;
				break;
			}

			j++;
		}

		while (tempWord[k] != '\0')
		{
			cout << tempWord[k];
			k++;
		}

		k = k + 1;
		cout << endl;
	}


	return 0;
}

