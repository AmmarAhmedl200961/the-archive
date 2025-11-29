#include <iostream>
using namespace std;

int digitSum(int);
int digitCount(int);
void reverseNum(int);
bool isEven(int);
int isMax(int, int, int, int, int, char);
int isCapital(char);
char highestAverage(int, int, int, int, int, int, char, char, char, char, char, char);
int calc(int, char, int);
int multipleChecker(int, int);
void quadDisplay(int);
float pointDistSqr(int, int, int, int);
int quadType(int, int, int, int, int, int, int, int);

int main1()
{
	int num, ans;
	cout << "\nAny digit number: ";
	cin >> num;
	ans = digitSum(num);
	cout << endl << "Sum of " << num << " is " << ans;

	return 0;
}

int main2()
{
	int num;
	cout << "\nNumber: ";
	cin >> num;
	cout << endl << "\nDigit count is: " << digitCount(num);
	cout << endl << "\nReverse is: "; reverseNum(num);

	return 0;
}

int main3()
{
	int num;
	bool ans;

	cout << "Number: ";
	cin >> num;
	if (isEven(num))
		cout << endl << num << " is Even...";

	else
		cout << endl << num << " is Odd...";

	return 0;
}

int main4()
{
	int n1, n2, n3, n4, n5;
	char m1 = 'f';
	char m2 = 's';
	cout << "Give 6 numbers: ";
	cin >> n1 >> n2 >> n3 >> n4 >> n5;

	cout << "\nFirst max: " << isMax(n1, n2, n3, n4, n5, m1) << "\nSecond Max: " << isMax(n1, n2, n3, n4, n5, m2);

	return 0;
}

int main5()
{
	char letter;
	cout << "\nEnter a letter: ";
	cin >> letter;

	if (isCapital(letter) == 1)
		cout << "\nIs Lower case letter\n";

	else if (isCapital(letter) == 2)
		cout << "\nIs Capital letter\n";

	else if (isCapital(letter) == 3)
		cout << "\nNone\n";

	return 0;
}

int main6()
{
	cout << "\nHighest Average Checker";
	char maxRn;
	int n1, n2, n3, n4, n5, n6;
	char a1, a2, a3, a4, a5, a6;
	cout << "\nEnter section and average 6 consecutively...";
	cin >> a1 >> n1 >> a2 >> n2 >> a3 >> n3 >> a4 >> n4 >> a5 >> n5 >> a6 >> n6;

	cout << "\nSection " << highestAverage(n1, n2, n3, n4, n5, n6, a1, a2, a3, a4, a5, a6) << " has the highest average...";

	return 0;
}

int main7()
{
	cout << "\nType of quadrilateral From Four Points";

	int x1, y1, x2, y2, x3, y3, x4, y4;
	cout << "\nEnter the 4 Points (x,y):\n ";
	cin >> x1 >> y1;
	cin >> x2 >> y2;
	cin >> x3 >> y3;
	cin >> x4 >> y4;

	int type = quadType(x1, y1, x2, y2, x3, y3, x4, y4);
	quadDisplay(type);

	return 0;
}

int main10()
{
	int N1, N2;
	char oper;
	cout << "\nEnter equation: ";
	cin >> N1 >> oper >> N2;
	cout << "\nAnswer is: " << calc(N1, oper, N2);

	return 0;
}

int main11()
{
	int a, b;
	cout << "\nEnter two numbers: ";
	cin >> a >> b;

	if (multipleChecker(a, b) == 1)
		cout << a << " is the multiple of " << b;
	else if (multipleChecker(a, b) == 2)
		cout << a << " is not a multiple of " << b;

	return 0;
}






int digitSum(int num)
{
	int sum = 0;
	int number = num;
	while (number != 0)
	{
		sum = sum + number % 10;
		number = number / 10;
	}

	return sum;
}

int digitCount(int num)
{
	int dig = 0;
	int number = num;
	while (number != 0)
	{
		number = number / 10;
		dig += 1;
	}

	return dig;
}

void reverseNum(int num)
{
	int count = digitCount(num);
	int n1 = num;


	while (count > 0)
	{
		cout << " " << n1 % 10;
		n1 = n1 / 10;
		count -= 1;
	}
}

bool isEven(int num)
{
	if (num % 2 == 0)
		return true;

	else
		return false;
}

int isMax(int n1, int n2, int n3, int n4, int n5, char m)
{
	int max;
	int maxsecond;

	max = n1;
	maxsecond = n1;

	if (max < maxsecond)
		max = maxsecond;

	if (max < n3)
		max = n3;

	if (max < n4)
		max = n4;

	if (max < n5)
		max = n5;

	if (maxsecond < n1 && n1 != max)
		maxsecond = n1;

	if (maxsecond < n2 && n2 != max)
		maxsecond = n2;

	if (maxsecond < n3 && n3 != max)
		maxsecond = n3;

	if (maxsecond < n4 && n4 != max)
		maxsecond = n4;

	if (maxsecond < n5 && n5 != max)
		maxsecond = n5;

	if (m == 'f')
		return max;

	else if (m == 's')
		return maxsecond;
	else
		cout << "Funtion only takes in char variable \n('f') for first max and\n('s') for second max... "
		<< "Please try again";
	return 0;

}

int isCapital(char letter)
{
	if (letter >= 'a' && letter <= 'z')
		return 1;
	else if (letter >= 'A' && letter <= 'Z')
		return 2;
	else
		return 3;
}

char highestAverage(int n1, int n2, int n3, int n4, int n5, int n6, char a1, char a2, char a3, char a4, char a5, char a6)
{
	int maxAvg = n1;
	char maxRn = a1;

	if (maxAvg < n2)
		maxAvg = n2,
		maxRn = a2;

	if (maxAvg < n3)
		maxAvg = n3,
		maxRn = a3;

	if (maxAvg < n4)
		maxAvg = n4,
		maxRn = a4;

	if (maxAvg < n5)
		maxAvg = n5,
		maxRn = a5;

	if (maxAvg < n6)
		maxAvg = n6,
		maxRn = a6;

	return maxRn;
}

int calc(int n1, char oper, int n2)
{
	float res;

	switch (oper)
	{
	case '+':
		res = n1 + n2;
		break;

	case '-':
		res = n1 - n2;
		break;

	case '*':
		res = n1 * n2;
		break;

	case '/':
		res = n1 / n2;
		break;

	case '%':
		res = n1 % n2;
		break;
	}

	return res;
}

int multipleChecker(int a, int b)
{
	if (a % b == 0)
		return 1;

	else
		return 2;
}

float pointDistSqr(int x1, int y1, int x2, int y2)
{
	int res;
	int deltaX = x2 - x1;
	int deltaY = y2 - y1;


	deltaX = deltaX * deltaX;
	deltaY = deltaY * deltaY;
	res = deltaX + deltaY;
	return res;
}

int quadType(int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4)
{
	int s1, s2, s3, s4, d1, d2;

	s1 = pointDistSqr(x1, y1, x2, y2);
	s2 = pointDistSqr(x2, y2, x3, y3);
	s3 = pointDistSqr(x3, y3, x4, y4);
	s4 = pointDistSqr(x4, y4, x1, y1);
	d1 = pointDistSqr(x1, y1, x3, y3);
	d2 = pointDistSqr(x2, y2, x4, y4);

	if (d1 == d2)
	{
		if (s1 == s2 && s2 == s3 && s3 == s4)
			return 1;

		else
			return 2;
	}

	else
	{
		if (s1 == s2 && s2 == s3 && s3 == s4)
			return 3;

		else
			return 4;
	}

	return 0;
}

void quadDisplay(int quad)
{
	switch (quad)
	{
	case 1:
		cout << "\nPoints make a Square";
		break;

	case 3:
		cout << "\nPoints make a Rhombus";
		break;

	case 2:
		cout << "\nPoints make a Rectangle";
		break;

	case 4:
		cout << "\nPoints make a Parallelogram";
		break;

	case 0:
		cout << "\nIrregular Quad";
		break;
	}
}