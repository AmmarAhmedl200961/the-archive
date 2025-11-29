#include <iostream>
using namespace std;

int main_10()
{
     // Problem 10
	cout << endl << "-Problem-10-" << endl;

	int BoxIter = 0;

	cout << "Enter a positive integer no greater than 15" << endl;
	cin >> BoxIter;

	for (int x = 1; x <= BoxIter; x++)
	{
		for (int y = 1; y <= BoxIter; y++)
		{
			cout << "X";
		}
		cout << endl;
	}
	
	return 0;
}


int main_9()
{
	// Problem 9
	cout << endl << "-Problem-9-" << endl;
	double cal;
	cal = 2.9;
	cout << endl << "Running on this treadmill you will burn " << cal << " calories per minute.";
	int table = 1;
	int min = 10;
	while (table <= 5)
	{
		cout << "\n" << "After " << min << " minutes you will burn " << cal * table << " calories." << "\n";
		min = min + 5;
		table = table + 1;
	}
	return 0;
}






int main_8()
{
	// Problem 8

	cout << endl << "-Problem-8-" << endl;
	double K;
	K = 2.5;
	cout << "Ocean level rises at " << K << " millimeters per year:  " << endl;


	int multiplier = 1;
	while (multiplier <= 15)
	{
		cout << "\n" << "Year " << multiplier << " = " << K * multiplier << "\n";
		multiplier += 1;
	}
	return 0;
}




int main_7()
{
	// Problem 7
	cout << endl << "-Problem-7-" << endl;
	int loop;
	int sum;
	double result;
	result = 0;
	sum = 0;
	cout << endl << "# of desired values:  ";
	cin >> loop;

	int k = 0;
	while (k < loop)
	{
		int value;
		cout << "Enter value  " << k + 1 << ":  ";
		cin >> value;
		sum = sum + value;
		k += 1;

	}


	result = sum / k;
	cout << endl << "Output of your desired values:  " << endl;
	cout << endl << "Average:  " << result << endl;
	cout << "Sum:  " << sum << endl;
	return 0;
}

int main_6()
{
	// Problem 6
	cout << endl << "-Problem-6-" << endl;
	int loops;
	double total = 0;

	cout << "Number of Integers to find sum of : " << endl;
	cin >> loops;

	int iter = 0;

	while (iter < loops)
	{
		int nums;
		nums = iter + 1;
		
		total = total + nums;
		iter += 1;

	}

	cout << endl << "Sum of your integers : " << total << endl;


	return 0;
}




int main_5()
{
	// Problem 5
	cout << endl << "-Problem-5-" << endl;
	double LoanPayment, Insurance, Gas, Oil, Tires, Maintenance;
	cout << "Your Loan payment, insurance, gas oil, tires and maintenance of your automobile succesively" << endl;
	cin >> LoanPayment >> Insurance >> Gas >> Oil >> Tires >> Maintenance;
	double TotalMonthly = LoanPayment + Insurance + Gas + Oil + Tires + Maintenance;
	double TotalYearly = TotalMonthly * 12;
	cout << endl << "Monthly Total:  " << TotalMonthly;
	cout << endl << "Yearly Total:  " << TotalYearly << endl;

	return 0;
}




int main_4()
{
	// Problem 4
	cout << endl << "-Problem-4-" << endl;
	double A = 0;
	double B = 0;
	double C = 0;
	double output;
	cout << endl << "Enter your rainfall value of 3 months:  ";
	cin >> A >> B >> C;
	output = (A + B + C) / 3;
	cout << endl << "Output:  " << output;
	return 0;
}




int main_3()
{
	// Problem 3
	cout << endl << "-Problem-3-" << endl;

	double gallons = 15.0;
	double distance = 35.0;
	double mpg;
	mpg = distance / gallons;
	cout << "Gallons =  " << gallons << endl << "Distance =  " << distance << endl << "mpg =  " << mpg;

	return 0;
}




int main_2()
{
	// Problem 2

	cout << endl << "-Problem-2-" << endl;
	int N1 = 24, N2 = 32, N3 = 37, N4 = 40, N = 4, Sum;
	double Average;

	Sum = N1 + N2 + N3 + N4;
	Average = 1.0 * Sum / N;

	cout << endl << "Sum of your numbers is : " << Sum << endl;
	cout << endl << "Average of your numbers is : " << Average << endl;






	return 0;
}




int main_1()
{
	//Problem 1b
	//1a was hardcoded so here I removed hardcoded values and adjusted for user inputs.

	cout << endl << "-Problem-1-(b)\n" << endl;

	float tax;
	float salestax;
	double price;
	float totaltax;
	                            
	cout << "Price:  ";
	cin >> price;
	                            //Shifted cout to cin.
	cout << "Country Tax % :  ";
	cin >> tax;
	tax = tax / 100;
	                           
	cout << "Sales Tax % :  ";
	cin >> salestax;
	salestax = salestax / 100;

	totaltax = price * (tax + salestax);

	cout << "Total tax =  " << totaltax << endl << "Total price =  " << totaltax + price;



	return 0;
}