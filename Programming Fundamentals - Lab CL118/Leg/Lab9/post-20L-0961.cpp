#include<iostream>
using namespace std;
void SWAP(char& A, char& B)
{
	int temp = B;
	B = A;
	A = temp;
}
void printCharArray(char A[])
{
	for (int i = 0; A[i] != '\0'; i++)
	{
		cout << A[i] ;
	}
	cout << endl;
}
int strlength(char A[])
{
	int strlength = 0;
    for (int i = 0; A[i] != '\0'; i++)
        strlength++;
    return strlength;

}
void Reverse(char A[], int si, int ei)
{
	for (si = si, ei = ei; si < ei; si++, ei--)
	{
		Swap(A[si], A[ei]);
	}
}
void reverseSentence(char S[])
{
	int size = strlength(S);
	int si = 0;
	int ei = size - 1;
	Reverse(S, si, ei);
	ei = 0;
	for (int i = 0; S[i] != '\0'; i++)
	{
		while (S[ei] != ' ' && ei <= size-1)
			ei++;
		Reverse(S, si, ei - 1);
		si = ei + 1;
		ei++;
	}
}
bool isPalindrome(char A[])
{
	bool palindrome = true;
	int size = strlength(A);
	int si = 0;
	int ei = size - 1;
	for (si = si, ei = ei; si < ei; si++, ei--)
	{
		if (A[si] != A[ei])
		{
			palindrome = false;
		}
	}
	return palindrome;
}
int stringToInteger(char S[])
{
	int value = 0;
	int size = strlength(S);
	for (int i = 0; i < size; i++)
	{
		value = value + (48 - S[i]);
		value *= 10;
	}
	value /= 10;
	if (value < 0)
		value = value * -1;
	return value;
}
bool substringSearch(char A[], char sub[])
{
	bool ans = false;
	int size = strlength(A);
	int size2 = strlength(sub);
	int ai = 0;
	int si = 0;
	while (A[ai] != sub[si])
		ai++;
	for ( ai = ai, si = si; si < size2; ai++, si++)
	{
		if (A[ai] == sub[si])
			ans = true;
		else
			ans = false;
	}
	return ans;

}
int firstSubstringSearch(char A[], char sub[])
{
	bool ans = false;
	int size = strlength(A);
	int size2 = strlength(sub);
	int ai = 0;
	int si = 0;
	while (A[ai] != sub[si])
		ai++;
	int temp = ai;
	for (ai = ai, si = si; si < size2; ai++, si++)
	{
		if (A[ai] == sub[si])
			ans = true;
		else
			ans = false;
	}
	if (ans == true)
		return temp;
	else
		return -1;
}
int lastSubstringSearch(char A[], char sub[])
{

	bool ans = false;
	int size = strlength(A);
	int size2 = strlength(sub);
	int ai = size-1;
	int si = 0;
	while (A[ai] != sub[si])
		ai--;
	int temp = ai;
	for (ai = ai, si = si; si < size2; ai++, si++)
	{
		if (A[ai] == sub[si])
			ans = true;
		else
			ans = false;
	}
	if (ans == true)
		return temp;
	else
		return -1;
}
int main_1()
{
	char A[] = { "test my be will This" };
	cout << "Before Reversal: ";
  printCharArray(A) ;
  cout << endl;
	reverseSentence(A);
	cout << "After Reversal: ";
	printCharArray(A);
	cout << endl;
	return 0;
}
int main_2()
{
	char A[] = { "civic" };
	cout << "Entered String is ";
		PrintCharArray(A);
		cout << endl;
	if (isPalindrome(A) == 1)
		cout << "Yes, String is Palindrome " << endl;
	else
		cout << "No, String is not Palindrome" << endl;
	return 0;
}
int main_3()
{
	char A[] = { "12345" };
	cout << "Entered String is: ";;
		PrintCharArray(A);
		cout << "Returned Integer value is ";
		cout << StringToInteger(A) << endl;
		return 0;
}
int main_4()
{
	char A[] = { "Reverse" };
	char B[] = { "verse" };
	cout << "Entered string A : ";
	printCharArray(A);
	cout << "Entered string B  : ";
	printCharArray(B);
	if (substringSearch(A,B) == 1)
		cout << "Yes, B is subset of A " << endl;
	else
		cout << "No, B is not subset of A" << endl;
	return 0;
}
int main_5()
{
	char A[] = { "Reverseverse" };
	char B[] = { "verse" };
	cout << "Entered string A : ";
	printCharArray(A);
	cout << "Entered string B  : ";
	printCharArray(B);
	if (firstSubstringSearch(A,B) == -1)
		cout << "No, B is not an even subset of A " << endl;
	else
		cout << "at index(first) "<< firstSubstringSearch(A, B) << " B is a subset of A" << endl;
	return 0;
}
int main_6()
{
	char A[] = { "Reverseverse" };
	char B[] = { "verse" };
	cout << "Entered string A : ";
	printCharArray(A);
	cout << "Entered string B  : ";
	printCharArray(B);
	if (lastSubstringSearch(A, B) == -1)
		cout << "No, B is not even a subset of A " << endl;
	else
		cout << "at index(last) " << lastSubstringSearch(A, B) << " B is a subset of A" << endl;
	return 0;
}
