#include <iostream>  
using namespace std;

int main()
{
	char str[100];
	
	cout << "Enter the string ";
	cin.get(str, 100);
	cin.ignore();
	

	int i = 0;
	while (str[i] != '\0')
	{
	
		if (str[i] >= 'a' && str[i] <= 'z')
			// lowercase to uppercase, 32 is the offset
			str[i] = str[i] - 32;
		else if (str[i] >= 'A' && str[i] <= 'Z')
			// uppercase to lowercase, 32 is the offset
			str[i] = str[i] + 32;

		i++;
	}

	cout << endl << str;
	
	return 0;
}