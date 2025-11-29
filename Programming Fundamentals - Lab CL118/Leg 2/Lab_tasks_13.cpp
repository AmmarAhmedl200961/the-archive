#include <iostream>
using namespace std;

void division(int a, int b) 
{
	cout << a / b;

}
void division(float a, float b) 
{
	cout << a / b;

}
void division(int a, int b, int c) 
{
	cout << a / b / c;

}
void division(double a, double b, double c) 
{
	cout << a / b / c;

}
void division(char a, char b) 
{
	cout << a / b;

}

int main()
{
	cin.get();

	int Ia, Ib, Ic;
	float Fa, Fb;
	double Da, Db, Dc;
	char Ca,Cb;

	char choice;
	int nums;

	cout << "\nenter numerical value for 2 / 3 and char value 2\n";
	
	cout << "I/i for int, F/f for floatm D/d for double, C/c for character\n ";

	cin >> choice;

	switch (choice)
	{
	case 'I': case'i':
	{
		cout << "enter amount of numbers ";
		cin >> nums;
		
		if (nums == 2)
		{
			cout << "int division a,b ";
			cin >> Ia >> Ib;
			division(Ia, Ib);
			
			cout << endl;
		}

		else if (nums == 3)
		{
			cout << "int division a,b,c ";
			cin >> Ia >> Ib >> Ic;
			division(Ia, Ib, Ic);
			cout << endl;
		}

	}	
	break;

	case'F':case'f':
	{
		cout << "float division a,b ";
		cin >> Fa >> Fb;
		division(Fa, Fb);
		
		cout << endl;
	}
	break;
	
	case'D': case'd':
	{
		cout << "double division a,b,c ";
		cin >> Da >> Db >> Dc;
		division(Da, Db, Dc);
		
		cout << endl;
	}
	break;

	case 'C': case 'c':
	{
		cout << "char division a,b ";
		cin >> Ca >> Cb;
		division(Ca, Cb);

		cout << endl;
	}

	default:
		break;
	}


	
	return 0;
}