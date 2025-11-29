#include<iostream>
using namespace std;

#include<conio.h>

int Reverse(int N)
{
	// 1234
	int Rev = 0;
	do
	{
		int r = N % 10;  // 4
		Rev = Rev * 10 + r;
		N = N / 10;      // 123
	} 
	while (N != 0);
	return Rev;
}

bool IsPalindrom(int N)
{
	// 121	1221	1345431	1111	1	2	3	321

	return N == Reverse(N);
}

int Decimal2BaseConvertor(int N, int b)
{
	int R = 0;
	bool started = false;
	int count = 0;
	do
	{
		if (started==false && N%b == 0)
		{
			count++;
		}
		else
		{
			started = true;
		}
		R = R * 10 + N % b;
		N = N / b;
	} 
	while (N != 0);

	R = Reverse(R);
	for (int i = 1; i <= count; i++)
	{
		R = R * 10;
	}
	return R;
}

int Power(int N, int K)
{
	int R = 1;
	for (int i = 1; i <= K; i++)
	{
		R *= N;
	}
	return R;
}

int CountDigits(int N, int b)
{
	int count = 0;
	do
	{
		N = N / b;
		count++;
	} 
	while (N != 0);
	return count;
}

int Decimal2BaseConvertor2(int N, int b)
{
	// int Count = CountDigits(N, b);
	int R = 0, count=0;
	do
	{
		R += (N%b) * Power(10, count);
		N = N / b;
		count++;
	} 
	while (N != 0);

	return R;
}

int FrogsJumpt(int H, int J, int S)
{
	int count = 0;
	
	if (H > J && J <= S)
		return -1;
	do
	{
		H = H - J;
		count++;
		if (H <= 0)
			return count;

		H = H + S;
	} 
	while (true);
}

/*
	1
	1 2
	1 2 3
	1 2 3 4
	1 2 3 4 5

*/

void Traingle1(int H)
{
	for (int ln = 1; ln <= H; ln++)
	{
		/*
			ln		Kahan Tak
			1		1
			2		2
			3		3
			4		4
			.........
			ln		ln
		*/

		for (int n = 1; n <= ln; n++)
		{
			cout << n << " ";
		}
		cout << endl;
	}
}

/*
H = 5
						ln		Spaces		Kahan Tak
- - - - 1				1		H-1			1 = 1*2 - 1
- - - 1 2 3				2		H-2			3 = 2*2 - 1
- - 1 2 3 4 5			3		H-3			5 = 3*2 - 1
- 1 2 3 4 5 6 7			4		H-4			7 = 4*2 - 1
1 2 3 4 5 6 7 8 9       ................................
						ln		H-ln			ln*2 - 1

*/



void Traingle2(int H)
{
	for (int ln = 1; ln <= H; ln++)
	{
		
		for (int n = 1; n <= H-ln; n++)
		{
			cout << " " << " ";
		}

		for (int n = 1; n <= ln*2-1; n++)
		{
			cout << n << " ";
		}
		cout << endl;
	}
}
int main()
{

	Traingle2(10);



	/*int H = 13, J = 12, S = 13;

	cout<<FrogsJumpt(H, J, S);
	*/_getch();

	//int N = 256;
	//int M = Decimal2BaseConvertor2(N,2);
	//cout << M << endl;  // 100000011
	//M = Decimal2BaseConvertor(N, 2);
	//
	//cout << M << endl;  // 100000011
	//_getch();
	return 0;
}