#include <iostream>
#include <math.h>
using namespace std;

void sequenceOdd(int);
void sequence_xFive(int);
void sequence_xThree(int);
void sequencePlusThree_TimesTwo(int);
void sequenceFive_Twelve_Half(int);
void sequenceDecreasing(int);
void sequenceDecreasingDivide2(int);
void sequence_Add2Add5(int);
void sequenceAlternates(int);
void sequence_2rep(int);
void sequence_2rep_r5r2(int);
void sequencelast(int);
void arePrime(int num);
void primeFactors(int);
int largestPrimeFactor(int);
void primesInBetween(int, int);

int p1(); int p2(); int p3(); int p4(); int p5();

void displaymenu()
{
	system("cls");
	cout << "-Problem-1-\Display following Sequences\n";
	cout << "-Problem-2-\Even Odd\n";
	cout << "-Problem-3-\Character Counter\n";
	cout << "-Problem-4-\nMinimum Maximum\n";
	cout << "-Problem-5-\nPrimes\n";

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

		}

		cout << "\n\n Do you want to continue ? (Y/y)";
		cin >> tocontinue;
	}

	return 0;

}

int p1()
{
	int n;
	cout << "Enter the number to print the sequences till..";
	cin >> n;
	sequencelast(n);
	cout << endl;


	return 0;
}

int p2()
{
	int i = 0;
	cout << "enter a set of even or odd numbers...";
	int evenCount; int oddCount;
	evenCount = oddCount = 0;


	while (i != -1)
	{
		cin >> i;

		if (i == -1)
			break;

		if (i % 2 == 0)
			evenCount += 1;
		else if (i % 2 != 0 && i != -1)
			oddCount += 1;
	}

	cout << "\ncount of even numbers  " << evenCount<< "\ncount of odd numbers  " << oddCount;

	return 0;
}

int p3()
{
	char i = 0;
	int consonCount;
	int voweCount;
	int otherCount;
	consonCount = voweCount = otherCount = 0;

	cout << "enter your is...";


	while (i != '$')
	{
		cin >> i;

		int toLower(i);

		if (i == '$')
			break;
		if (i == 'a' ||i=='e'|| i == 'i' || i == 'o' || i == 'u')
			voweCount += 1;
		else if ((i > 'a' && i < 'e') || (i > 'e' && i < 'i') || (i > 'i' && i < 'o') || (i > 'o' && i < 'u') || (i > 'u' && i <= 'z'))
			consonCount += 1;
		else if (((i < 'a' && i > 'Z') || (i < 'A') || (i > 'z')) && i != '$')
			otherCount += 1;



	}

	cout << "\ncount of vowels  " << voweCount << endl;
	cout << "\ncount of consonants  " << consonCount << endl;
	cout << "\ncount of other is  " <<otherCount<< endl;


	return 0;
}

int p4()
{
	//found online
	
	int num;
	int min, max;
	cout << "nums:\n";
	cin >> num;
	min = num;
	max = num;

	do
	{
		cin >> num;

		if (num == -1)
		{
			cout << "\nMax: " << max << endl;
			cout << "Min: " << min << endl;
		}


		else if (max < num)
			max = num;

		else if (min > num)
			min = num;

	} while (num != -1);

}

int p5()
{
	//found online
	
	int n1, n2;
	cin >> n1 >> n2;
	primesInBetween(n1, n2);

	return 0;

}

/*--FUNCTIONS--*/

void sequenceOdd(int n)
{
	int k = 1;
	while (n > 0)
	{
		cout << k << ", ";
		k += 2;
		n --;
	}
}

void sequence_xFive(int n)
{
	cout << "1, ";

	int k = 5;
	while (n >= 1)
	{
		cout << k * 5 << ",";
		k = k * 5;
		n --;
	}
}

void sequence_xThree(int n)
{
	cout << "1, ";

	int k = 3;
	while (n >= 1)
	{
		cout << k * 3 << ",";
		k = k * 3;
		n--;
	}
}

void sequencePlusThree_TimesTwo(int n)
{
	cout << "1 ";

	int k = 1;
	while (n >= 1)
	{
		cout << k + 3 << ",";
		k = k + 3;

		cout << "," << k * 2 << ",";
		k = k * 2;

		n -= 3;
	}
}

void sequenceFive_Twelve_Half(int n)
{
	cout << "1,";

	int k=1;
	while (n >= 1)
	{
		cout << n + 3 << ",";
		k = k + 3;

		cout << n * 2 << ",";
		k = k * 2;

		n -= 3;
	}
}

void sequenceDecreasing(int n)
{
	for (int k = n; k >= 0; k--)
	{
		cout << k << ",";
	}
}

void sequenceDecreasingDivide2(int n)
{
	for (int k = n; k > 0;)
	{
		cout << k << ",";
		k = k / 2;
	}
}

void sequence_Add2Add5(int n)
{
	int n1 = 1;
	int n2 = 1;
	cout << endl;

	for (int k = n; k > 0; k -= 2)
	{
		cout << n1 << "," << n2 << ",";
		n1 += 2;
		n2 += 5;
	}
}

void sequenceAlternates(int n)
{
	int n1 = n;
	int n2 = 1;

	;
	for (int k = n / 2; k > 0; k--)
	{
		cout << n1 << "," << n2 ;
		n1 -= 1;
		n2 += 1;
	}
	
	if (n % 2 != 0)
		cout << "," << n / 2 + 1;
}

void sequence_2rep(int n)
{
	int n1 = 0;
	int n2 = 0;

	for (int k = n; k > 0; k -= 2)
	{
		cout << n1 << "," << n2 << ",";
		n1 += 4;
		n2 += 8;
	}
}

void sequence_2rep_r5r2(int n)
{
	int n1 = 10;
	int n2 = 20;

	for (int k = n; k > 0; k -= 2)
	{
		cout << n1 << "," << n2 << ",";
		n1 += 5;
		n2 += 2;
	}
}

void sequencelast(int n)
{
	int n1 = 1;
	int n2 = 1;
	int mul = 2;
	int plu = 3;

	cout << "1, 1" << endl;

	for (int k = n; k > 1; k -= 2)
	{
		cout << n1 << "," << n2 << ",";
		n1 = mul * n1;
		n2 = n2 + plu;
		mul += 1;
		plu += 2;
		
	}
}



void arePrime(int num)
{
	int test;
	cout << "nums:\n";
	for (int i = 0; i < num; i++)
	{
		cin >> test;
		bool prime = true;

		if (test == 1)
			prime = false;

		if (test == 2)
			prime = true;

		else if (test % 2 == 0)
			prime = false;

		int  j = 3; int k = sqrt(test);
		while (j < k && test > 2)
		{
			if (k % j == 0)
			{
				prime = false;
				break;
			}
			i += 2;
		}
		if (prime)
			cout << "Prime\n";

		else
			cout << "NotPrime\n";
	}
}

void primeFactors(int num)
{

	int i;
	cout << "Factors:\n";

	while (num % 2 == 0)
	{
		cout << ' ' << 2;
		num = num / 2;
	}

	for (i = 3; i < sqrt(num); i += 2)
	{
		while (num % i == 0)
		{
			cout << ' ' << i;
			num = num / i;
		}
	}

	if (num > 2)
		cout << ' ' << num;

}

int largestPrimeFactor(int num)
{
	int i;
	int max = num;

	while (num % 2 == 0)
	{
		num = num / 2;
		max = 2;
	}

	for (i = 3; i < sqrt(num); i += 2)
	{
		while (num % i == 0)
		{
			max = i;
			num = num / i;
		}
	}
	if (num > 2)
	{
		max = num;
	}

	return max;
}

void primesInBetween(int n1, int n2)
{
	for (int i = n1; i <= n2; i++)
	{
		bool prime = true;

		if (i == 1)
			prime = false;

		if (i == 2)
			prime = true;

		else if (i % 2 == 0)
			prime = false;

		int  z = 3; int k = sqrt(i);
		while (z < k && i > 2)
		{
			if (k % z == 0)
			{
				prime = false;
				break;
			}
			z += 2;
		}
		if (prime)
			cout << i << ' ';
	}
}
