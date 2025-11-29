#include <iostream>
using namespace std;

void changeCase(char s[])
{
	for (int i = 0; s[i] != '\0'; i++)
	{
		if (s[i] > 64 && s[i] < 91) //range of upper case 
		{
			s[i] += 32; //offset of lower characters
		}
		else if (s[i] > 96 && s[i] < 123) //range of lower case 
		{
			s[i] -= 32; //offset of upper characters
		}
	}
}


int main()
{
	char s[100];

	cout << "character array to capitalize / uncapitalise ";
	cin.getline(s, 100);

	changeCase(s);

	cout <<"after changes "<< s;


	return 0;
}