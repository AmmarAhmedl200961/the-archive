#include <iostream>
using namespace std;

bool iseven(int);
int charchecker(char);
char highestaggre(int, int, int, int, int, int, char, char, char, char, char, char);
float calc(int, char, int);
int multipleof(int, int);
int DigitCount(int);
void ReverseNum(int);
bool IsCompound(int);
bool isPrime(int);
int DistanceSquare(int, int, int, int);
int QuardilateralType(int, int, int, int, int, int, int, int);
void PrintQuardType(int);
int floorNum(float);
int ceilNum(float);

int p1(); int p2(); int p3(); int p4(); int p5(); int p6(); int p7(); int p8(); int p9(); int p10();


void displaymenu()
{
	system("cls");
	cout << "-Problem-1-\nEven or Odd number\n";
	cout << "-Problem-2-\nletter Checker\n";
	cout << "-Problem-3-\nHighest Aggregate\n";
	cout << "-Problem-4-\nCalculator\n";
	cout << "-Problem-5-\nCheck for multiplicity of two numbers\n";
	cout << "-Problem-6-\nDigit Counter and Reverser\n";
	cout << "-Problem-7-\nCompound Number Checker\n";
	cout << "-Problem-8-\nPrime Number Checker\n";
	cout << "-Problem-9-\nCheck for quadrilateral\n";
	cout << "-Problem-10-\nCeil and Floor a number\n";
}

int main()
{
	int option;
	char tocontinue = 'Y';
	while (tocontinue == 'y' || tocontinue == 'Y')
	{
		displaymenu();
		cin >> option;
		switch (option)
		{
		case 1:
			 p1();
			break;
		case 2:
			 p2();
			break;
		case 3:
			 p3();
			break;
		case 4:
			 p4();
			break;
		case 5:
			 p5();
			break;
		case 6:
			 p6();
			break;
		case 7:
			 p7();
			break;
		case 8:
			 p8();
			break;
		case 9:
			 p9();
			break;
		case 10:
			 p10();
			break;

		}

		cout << "\n\n Do you want to continue ? (Y/y)";
		cin >> tocontinue;
	}
	
	return 0;

}


int p1()
{
	int num;
	cout << "number  ";
	cin >> num;

	if (iseven(num))
		cout << "is even  ";
	else
		cout << "odd number  ";
	
	return 0;
}

int p2()
{
	char chtr;
	cout << "enter your character  ";
	cin >> chtr;
	int ans = charchecker(chtr);

	if (ans == 1)
		cout << "capital letter" << endl;
	if (ans == 2)
		cout << "small letter" << endl;
	if (ans == 3)
		cout << "none" << endl;

	return 0;
}

int p3()
{
	char maxres;
	int n1, n2, n3, n4, n5, n6;
	char x1, x2, x3, x4, x5, x6;

	cout << "enter section and highest average consecutively";
	cin >> x1 >> n1 >> x2 >> n2 >> x3 >> n3 >> x4 >> n4 >> x5 >> n5 >> x6 >> n6;
	cout << "highest aggregate is  ";
	highestaggre(x1, x2, x3, x4, x5, x6, n1, n2, n3, n4, n5, n6); 

	return 0;
}

int p4()
{
	int v1, v2;
	char oper;
	cout << "enter two numbers to calculate followed by operator  ";
	cin >> v1 >> oper >> v2;
	cout << "answer is  " << calc(v1, oper, v2);

	return 0;
}

int p5()
{
	int a, b;
	cout << "enter two multiples of each other  ";
	cin >> a >> b;

	if (multipleof(a, b))
		cout << a << "  is a multiple of  " << b;

	return 0;
}

int p6()
{
	int num;
	cout << "enter a number to reverse and count  ";
	cin >> num;
	cout << " digits count is  " << DigitCount(num) << endl;
	cout << " reverse is  ";
	ReverseNum(num);

	return 0;
}

int p7()
{
	int num3;
	cout << "to check coumpound number" << endl;
	cin >> num3;

	if (IsCompound(num3))
		cout << "compound number  ";
	else
		cout << "not a compound number  ";

	return 0;
}

int p8()
{
	int num4;

	cout << "Enter a positive integer: ";
	cin >> num4;

	bool prime = isPrime(num4);

	if (prime) {
		cout << "Prime Number.";
	}
	else {
		cout << "Not a Prime Number.";
	}

	return 0;
}

int p9()
{
	int p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y;
	
	cin >> p1x >> p1y
		>> p2x >> p2y
		>> p3x >> p3y
		>> p4x >> p4y;

	int qt = QuardilateralType(p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y);

	PrintQuardType(qt);

	return 0;
}

int p10()
{
	float n;

	cout << "Enter a number for floor: ";
	cin >> n;

	cout << "Floored number: " << floor(n) << endl;

	cout << "Enter a number for ceil: ";
	cin >> n;

	cout << "Ceiled number: " << ceil(n) << endl;

	return 0;
}


bool iseven(int x)
{
	if (x % 2 == 0)
		return true;
	else
		return false;
}

int charchecker(char chtr)
{
	int ans;
	if (chtr >= 'A' && chtr <= 'Z')
		ans = 1;
	else if (chtr >= 'a' && chtr <= 'z')
		ans = 2;
	else
		ans = 3;

	return ans;
}

char highestaggre(int n1, int n2, int n3, int n4, int n5, int n6, char x1, char x2, char x3, char x4, char x5, char x6)
{
	int maxavg = n1;
	char maxres = x1;

	if (maxavg < n2) {
		maxavg = n2;
		maxres = x2;
	}

	if (maxavg < n3) {
		maxavg = n3;
		maxres = x3;
	}

	if (maxavg < n4) {
		maxavg = n4;
		maxres = x4;
	}

	if (maxavg < n5) {
		maxavg = n5;
		maxres = x5;
	}

	if (maxavg < n6) {
		maxavg = n6;
		maxres = x6;
	}

	return maxres;

}

float calc(int v1, char oper, int v2)
{
	float res=0;
	switch (oper)
	{
	case'x':
		res = v1 * v2;
		break;

	case'+':
		res = v1 + v2;
		break;

	case'/':
		res = v1 / v2;
		break;

	case'-':
		res = v1 - v2;
		break;

	case'%':
		res = v1 % v2;
		break;


	}
	return res;
}

int multipleof(int a, int b)
{
	if (a % b == 0)
		return true;
	else
		return false;
}

int DigitCount(int num2)
{
	int digit = 0;
	int num = num2;
	while (num != 0)
	{
		num = num / 10;
		digit++;
	}
	return digit;
}

void ReverseNum(int num)
{
	int res = 0;
	int count = DigitCount(num);
	int n1 = num;
	while (count > 0)
	{
		cout << " " << n1 % 10;
		n1 = n1 / 10;
		count--;
	}
}

bool IsCompound(int num)
{
	int n = 3;
	if (num == 1 || num == 2)
		return false;
	else if (num % 2 == 0)
		return true;
	while (n < num)
	{
		if (num % n == 0)
			return true;
		n = n + 2;
	}
	return true;
}

bool isPrime(int n)
{
	bool prime = true;

	if (n == 0 || n == 1)
	{
		prime = false;
	}
	else
	{
		for (int i = 2; i <= n / 2; i++)
		{
			if (n % i == 0)
			{
				prime = false;
				break;  // can break a loop
			}
		}
	}
	return prime;
}

int DistanceSquare(int x1, int y1, int x2, int y2)
{
	return (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1);
}

int QuardilateralType(int p1x, int p1y, int p2x, int p2y, int p3x, int p3y, int p4x, int p4y)
{
	int d1 = DistanceSquare(p1x, p1y, p2x, p2y);
	int d2 = DistanceSquare(p2x, p2y, p3x, p3y),
		d3 = DistanceSquare(p3x, p3y, p4x, p4y),
		d4 = DistanceSquare(p4x, p4y, p1x, p2y);

	int dg1 = DistanceSquare(p1x, p1y, p3x, p3y),
	dg2 = DistanceSquare(p2x, p2y, p4x, p4y);

	if (dg1 == dg2)
	{
		if (d1 == d2 && d2 == d3 && d3 == d4)
		{
			return 0;
		}

		else
		{
			return 1;
		}
	}
	else
	{
		if (d1 == d2 && d2 == d3 && d3 == d4)
		{
			return 2;
		}
		else if (d1 == d3 && d2 == d4)
		{
			return 3;
		}
		else
		{
			return 4;
		}
	}

}

void PrintQuardType(int qt)
{
	switch (qt)
	{
	case 0:
		cout << "Square  " << endl; 
		break;
	case 1:
		cout << "Rectangle  " << endl;
		break;
	case 2:
		cout << "Rhombus  " << endl;
		break;
	case 3:
		cout << "Parallelogram  " << endl;
		break;
	case 4:
		cout << "Quadrilateral  " << endl;
		break;


	default:
		break;
	}
}

int floorNum(float n)
{
	int f = n;
	if (n < 0 && f != n) {
		f--;
	}
	return f;
}

int ceilNum(float n)
{
	int c = n;
	if (n > 0 && c != n) {
		c++;
	}
	return c;
}
