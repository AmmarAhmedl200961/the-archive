// Ammar Ahmed		20L-0961		Assignment 1 //

#include <iostream>
using namespace std;

int main()
{
	int ft, yd, in;
	cout << "Enter your inches ";
	cin >> in;

	yd = in / 36;	//1 yd = 36 in/3 ft
	ft = in / 12;	//1 ft = 12 in, 36 in for example ???
	in = in % 12;	//remainder of ft calculated

	cout << yd << " yard " << ft << " feet " << in << " inches ";

	return 0;
}