// Ammar Ahmed		20L-0961		Assignment 1 //

#include <iostream>
using namespace std;

int main()
{
	int  unit = 100;	// for easiness unit price is harcoded
	double savings, price, net, quant;
	cout << "This program will give discount at < 1000 purchase\nEach unit is 100" << endl;
	
	cin >> quant;

	price = quant * unit;


	if (price < 0)		//check for incorrect amount entered
	{
		cout << "sorry, invalid amount of units entered";
	}

	else if (price > 1000)
	{
		cout << "eligible for 10 % discount..." << endl;
		savings = price * 0.1;
		net = price - savings;
		cout << "you pay " << net;
	}

	else
	{
		cout << "you pay " << price;
	}

	return 0;

}