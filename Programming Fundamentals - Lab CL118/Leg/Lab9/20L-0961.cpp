#include <iostream>
using namespace std;

int strLength(char []);
int indexOf(char[], char);

int main()
{
    const int asize = 500;
    char a[asize] = { "this will be my test" };
    cout << "\n" << "Your string length is:  " << strlength(a) << "\n";
}

int main_1()
{
	char A[] = { "this will be my test" };
	cout << "Your string length is:  " <<  strlength(A);
	return 0;
}
int main_2()
{
	char A[] = { "thiswillbemytest" };
	char c;
	cin >> c;
	cout << "Index of " << c << "in the array will be" << indexOf(A,c) ;
	return 0;
}
int main_3()
{
	char A[] = { "thiswillbemytest" };
	const int capacity = 100;
	char c;
	int Occurences[capacity];
	int OccSize = 0;
	cin >> c;
	allIndecesOf(A, c, Occurence, OccSize);
	cout << "The indeces are ";
	printArray(Occurence, OccSize);
	cout << "The character has occured " << OccSize << " In the array";
	return 0;
}

int main_4()
{
	char A[] = { "thiswillbemytest" };
	char c;
	cin >> c;
	removeFirstCharacter(A, c);
	printCharArray(A);
	return 0;
}
int main_5()
{
	char A[] = { "thiswillbemytest" };
	char c;
	cin >> c;
	removeLastCharacter(A, c);
	printCharArray(A);
	return 0;
}

int main_6()
{
	char A[] = { "thiswillbemytest" };
	char c;
	cin >> c; 
	removeAllCharacter(A, c);
	printCharArray(A);
	return 0;
}
int main_8()
{
	char A[] = { "abcdabcdabcd" };
	int si, ei;
	cin >> si >> ei;
	Reverse(A, si, ei);
	printCharArray(A);
}

void SWAP(char& A, char& B)
{
	int temp = B;
	B = A;
	A = temp;
}
void Reverse(char A[], int si, int ei)
{
	for (si = si, ei = ei; si < ei; si++, ei--)
	{
		SWAP(A[si] , A[ei]);
	}
}

void printCharArray(char A[])
{
	for (int i = 0; A[i]!='\0'; i++)
	{
		cout << A[i] << " ";
	}
	cout << endl;
}

void printArray(int A[],int Size)
{
	for (int i = 0; i<Size ; i++)
	{
		cout << A[i] << " " ;
	}
	cout << endl;
}

int strLength(char A[])
{
    int strlength = 0;
    for (int i = 0; A[i] != '\0'; i++)
        strlength++;
    return strlength;
}

int indexOf(char A[], char c)
{
	int dex = -1;
	for (int i = 0; A[i] != '\0'; i++)
	{
		if (A[i] == 'c')
		{
			dex = i;
			return dex;
		}
	
	}		
	return dex;
}

void allIndecesOf(char A[], char c, int Occurence[], int& OccSize)
{
	for (int i = 0; A[i] != '\0'; i++)
	{
		if (A[i] == c)
		{
			Occurence[OccSize] = i;
			OccSize++;
		}
	}
}

void removeFirstCharacter(char A[], char c)
{
	for (int i = 0; i != -1 ; i++)
	{
		if (A[i] == c)
		{
			do
			{
				A[i] = A[i + 1];
				i++;
			}
			while (A[i] != '\0');
			
			break;
		}

	}
}

void removeLastCharacter(char A[], char c)
{
	for (int i = 8; i != -1; i--)
	{
		if (A[i] == c)
		{
			do
			{
				A[i] = A[i + 1];
				i++;
			}
			while (A[i] != '\0');

			break;
		}

	}
}

void removeAll(char A[], char c)
{
	for (int i = 0; A[i] != '0'; i++)
	{
		int temp;
		if (A[i] == c)
		{
			temp = i-1;
			do
			{
				A[i] = A[i+ 1];
				i++;
			}
			while (A[i] != '\0');
			
			i = temp;
		}

	}
}
