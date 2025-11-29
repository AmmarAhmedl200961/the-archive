// Ammar Ahmed		20L-0961		Assignment 1 //

#include <iostream>
using namespace std;

int main()
{
	int DAYS,				//Days for input, will change
		dd, mm, yyyy;		
	cout << "Input days: ";
	cin >> DAYS;

	yyyy = DAYS / 365;
	DAYS %= 365;			//same as days = days%365, finds after-year remaining days 
	mm = DAYS / 30;			//simple remaining days to months conversion
	dd = DAYS % 30;			//remaider of days left from calculating months
	
	cout << yyyy << " years " << mm << " months " << dd << " days";

	return 0;
}