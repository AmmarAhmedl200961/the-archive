// Ammar Ahmed		20L-0961		Assignment 2, Question 4 //
#include <iostream>
#include <conio.h>
using namespace std;

void predictiveText(char words[][21], char in[], int iter)
{
	int r = 20;
	int chk = 0;

	for (int i = 0; i < r; i++) 
	{
		for (int j = 0; j < iter; j++) 
			if (in[j] == words[i][j]) 
				chk++;
		
		if (chk == iter) 
			cout << endl << words[i];
		chk = 0;
	}

}

void output(int wcount, char arr[])
{
	for (int i = 0; i < wcount; i++)
		cout << arr[i];
}

void input()
{
	system("cls");
	cout << ">>>";
}

int main() {
	char words[20][21] = {
						"apply",
						"application",
						"bat",
						"batch",
						"battle",
						"compute",
						"computer",
						"compare",
						"device",
						"develop",
						"developer",
						"function",
						"functional",
						"fucntionality",
						"handle",
						"handler",
						"handling",
						"system",
						"systemic",
						"systole"
	};

	// using a character array
	char a[21] = { 0 };
	int i = 0;
	int count = 0;
	while (true) {
		// if entered count is trigerred
		a[i] = _getch();
		++count;

		// simple functions to call input line in cmd followed by output of character array
		input();
		output(count, a);


		if (a[i] == 13) {//if ENTER pressed
			system("cls");
			cout << "Enter pressed" << endl;
			i = 0, count = 0;
		}
		else if (a[i] == '0')
			break;
		
		// if everything proceeds till this point call a 2d array substring check function
		else
			predictiveText(words,a,count);
		++i;
	}
	cout << endl << "<program terminated>" << endl;



	return 0;
}