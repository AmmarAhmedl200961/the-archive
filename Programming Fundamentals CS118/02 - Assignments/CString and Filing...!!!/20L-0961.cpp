#include <iostream>
#include <fstream>
using namespace std;

void Printer(char A[])
{
	for (int i = 0; A[i] != '\0'; i++)
		cout << A[i];
}

int StrLen(char A[])
{
	int count = 0;
	while (A[count] != '\0')
		count++;
	return count;
}

int CountWords(char A[])
{
	int sz = StrLen(A);
	int wordCount = 0;
	int startingI = 0;
	while (A[startingI] == ' ')  //Helps ignore spaces before first word
		startingI++;
	if (startingI == sz)
		return 0;
	for (int i = startingI; i < sz; i++)
	{
		if (A[i] == ' ')
		{
			wordCount++;
			if (A[i] == ' ')
				i++;
		}
	}
	if (A[sz - 1] != ' ') //will check the last index, if there is no space it iters the word count
		wordCount++;

	return wordCount;
}

void printing(int A[], int sz)
{
	for (int i = 0; i < sz; i++)
		cout << A[i] << ' ';
	cout << "\n";
}

void filePrinting(int A[], int sz)
{
	ofstream fout("output.txt");
	for (int i = 0; i < sz; i++)
		fout << A[i] << ' ';
	fout << "\n";
}

void LoadData(int A[], int& sz)
{
	ifstream fin("numbers.txt");

	fin >> sz;

	for (int i = 0; i < sz; i++)
		fin >> A[i];
}

int main()
{
	ifstream Rdr("sentences.txt");
	int sentenceCount;
	Rdr >> sentenceCount;
	Rdr.ignore(); // ignores the said line
	for (int i = 1; i < sentenceCount; i++)
	{
		char sentenceA[100];
		Rdr.getline(sentenceA, 100);
		cout << sentenceA << "\nCount of Words:  ";
		cout << CountWords(sentenceA) << "\n";
	}
	
	// some file stream basics
	const int capacity = 100;
	int sz;
	int A[capacity];
	/*ifstream fin("numbers.txt");
	ofstream fout("output.txt");

	fin >> sz;

	for (int i = 0; i < sz; i++)
		fin >> A[i];*/

	LoadData(A, sz);
	printing(A, sz);
	filePrinting(A, sz);

	// implementation of word count
	char sentence[] = { "Hi I am Ammar" };
	cout << sentence << "\n";
	cout << CountWords(sentence) << "\n\n";

	// cstring and character array
	int B[10] = { 1,2,3,0,20 };
	char C[10] = { "AMMAR" };

	for (int i = 0; i < 3; i++)
		cout << B[i] << " ";
	cout << "\n";

	cout << C << endl;

	return 0;
}