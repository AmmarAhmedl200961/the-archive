#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
using namespace std;

// Task 2

int main()
{
	char filename[20] = "inventory.txt";
	char name[10][15];
	int quantity[10];
	float price[10];
	int n = 10;							// the no. of products to read

	ifstream infile(filename);
	if (!infile.is_open())				// another approach to check file availability
	{
		cout << "Could not open input file " << filename << endl;
		return 1;
	}

	// Reading product details
	cout << left << setw(7) << "Code" << setw(15) << "Name" << setw(10) << "Quantity" << setw(10) << "Price" << endl;
	for (int i = 0; i < n; i++)
	{
		infile >> name[i] >> quantity[i] >> price[i];
		cout << setw(7) << (i + 1) << setw(15) << name[i] << setw(10) << quantity[i] << setw(10) << price[i] << endl;

	}
	infile.close();
	cout << endl;



	string bill = "";
	int code;
	float total = 0, subtotal;
	string ans;
	do
	{
		cout << "Enter the code of the item to buy [1- 10]: ";
		cin >> code;
		if (code < 1 || code > n)
			cout << "Invalid code " << endl;
		else
		{
			int qty;
			cout << "How many ? ";
			cin >> qty;
			subtotal = qty * price[code - 1];
			total += subtotal;
			quantity[code - 1] -= qty;				
			bill = bill + name[code - 1] + " " + to_string(qty) + " @ $" + to_string(price[code - 1]) + " = " + to_string(subtotal) + "\n";
												// converts an integer to a	string, helpful in our case.	
		}

		cout << "Do you want to buy more y/n ? ";
		cin >> ans;

	} while (ans == "y" || ans == "Y");

	cout << "Your bill is " << endl << bill << "Total $" << total << endl;

	// update the file

	ofstream outfile(filename);

	for (int i = 0; i < n; i++)
		outfile << name[i] << " " << quantity[i] << " " << price[i] << endl;
	
	outfile.close();
}
