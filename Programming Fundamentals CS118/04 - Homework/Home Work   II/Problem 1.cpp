// Ammar Ahmed		20L-0961		Home Work - II //

#include <iostream>
#include <string>
using namespace std;

string removeDoubledLetters(string s) 
{
	string fin = "";									// Initializing  returntype
	
	for (int i = 0; i < s.size(); i++) 
	{
		fin += s[i]; 

		while (i < (s.size() - 1) && s[i] == s[i + 1]) // Loop will check for similarity in next letter of string
			i++;									   // and will remove it with fin returntype
		
		

	} 
	
	return fin;
}

int main()
{
	cout << "enter string to remove doubled letters from\n";
	string s; 
	cin >> s;
	cout << removeDoubledLetters(s) << endl;
	
	return 0;
}