// Ammar Ahmed		20L-0961		Assignment 1 //

#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	double u = 1.234, p = 3.334;
	double i = 0;
	cout << "Enter your Value 'i'  \n"
	cin >> i;

	double res;
	res = (sqrt((u * ((float)pow(i, 1.5))) * ((pow(i, 2) - 1))))	//numerator part
		/ (sqrt((p * (i)-2)) + sqrt((p * (i)-1)));					//denominator part
	
	cout << "Processing Equation... \n";
	
	cout << res;
}