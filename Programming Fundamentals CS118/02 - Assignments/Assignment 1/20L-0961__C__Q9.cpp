// Ammar Ahmed		20L-0961		Assignment 1 //

#include <iostream>
using namespace std;

int main()
{
	char ch;
	
	cout << "Program will find 3rd next character" << endl
		 << "Enter your Charater  ";
	
	cin >> ch;
	ch = (int)ch + 3;	//type casting to int to add 3 ASCII
	
	cout << "\nYour Character  "<<(char)ch;	//type casting to char to find resultant character
	
	return 0;
}