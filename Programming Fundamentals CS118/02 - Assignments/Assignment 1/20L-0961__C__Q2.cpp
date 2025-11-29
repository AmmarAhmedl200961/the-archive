// Ammar Ahmed		20L-0961		Assignment 1 //

#include <iostream>
using namespace std;

int main()
{
	int hrWage, numHrs, tax;
	cout << "Enter hourly wage: ";
	cin >> hrWage;
	cout << "Enter number of hours: ";
	cin >> numHrs;
	cout << "Enter witholding tax: ";
	cin >> tax;
	int netPay, percentDeduct, totalWage;

	totalWage = numHrs * hrWage;
	percentDeduct = totalWage * ((float)tax / 100);		// we have to convert to a real value as 0.25 will be used (not 1)
	netPay=totalWage-percentDeduct;

	cout << "Net Pay:  " << netPay;
}