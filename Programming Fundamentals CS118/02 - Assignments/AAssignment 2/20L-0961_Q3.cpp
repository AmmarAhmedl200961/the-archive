// Ammar Ahmed		20L-0961		Assignment 2, Question 3 //
#include <iostream>
using namespace std;

void gridOut(char grid[][10])
{
	int r = 10, c = 10;

	cout << "   ";
	for (int i = 0; i < r; i++)
		cout << i << "   ";
	cout << endl;
	cout << " ";
	for (int i = 0; i < r; i++)
		cout << "____";
	cout << endl;

	for (int i = 0; i < r; i++)
	{
		cout << i << "| ";
		for (int j = 0; j < c; j++)
		{
			cout << grid[i][j] << "   ";
		}
		cout << endl;
	}
}

void wordOut(char words[][11])
{
	for (int i = 0; i < 15;)
	{
		
		for (int j = 0; j < 5; j++)
			cout << words[i++] << "\t";
		
		cout << endl;
	}
}

int wordCount(char words[][11], int i)
{
	int counter = 0;
	for (; words[i][counter] != '\0'; ++counter);
	return counter;

}

void find(char grid[][10], char words[][11])
{
	int wordR = 15, gridR, gridC;
	gridR = gridC = 10;

	for (int i = 0; i < gridR; i++)
	{
		for (int j = 0; j < gridC; j++)
		{
			for (int k = 0; k < wordR; k++)
			{
				if (grid[i][j] == words[k][0])
				{
					//check horizontal vertical and diagonal
					for (int l = 1; l <= wordR; l++)
					{
						if (
							//break if no word was found
							grid[i - l][j] != words[k][l] &&
							grid[i + l][j] != words[k][l] &&
							grid[i][j + l] != words[k][l] &&
							grid[i][j - l] != words[k][l] &&
							grid[i + l][j + l] != words[k][l] &&
							grid[i - l][j - l] != words[k][l] &&
							grid[i + l][j - l] != words[k][l] &&
							grid[i - l][j + l] != words[k][l])
						{
							break;
						}
						else if (l == wordCount(words, k))
						{
							cout << words[k] << " found at :\t( " << j + 1 << ", " << i + 1 << ")" << endl;
						}
					}
				}
			}
		}
	}
}

int main() {

	char grid[10][10] = {
						{ 'T', 'N', 'E', 'M', 'N', 'G', 'I', 'S', 'S', 'A'},
						{ 'B', 'N', 'C', 'A', 'O', 'M', 'P', 'J', 'W', 'R'},
						{ 'C', 'L', 'A', 'R', 'I', 'F', 'Y', 'H', 'X', 'R'},
						{ 'L', 'O', 'S', 'C', 'T', 'G', 'H', 'C', 'E', 'V'},
						{ 'A', 'N', 'M', 'H', 'S', 'Y', 'S', 'T', 'E', 'M'},
						{ 'S', 'T', 'I', 'P', 'E', 'Q', 'N', 'A', 'F', 'E'},
						{ 'S', 'S', 'E', 'Q', 'U', 'E', 'N', 'C', 'E', 'M'},
						{ 'U', 'E', 'F', 'N', 'Q', 'T', 'G', 'Q', 'W', 'O'},
						{ 'D', 'K', 'R', 'O', 'W', 'T', 'E', 'N', 'K', 'R'},
						{ 'A', 'O', 'M', 'O', 'D', 'N', 'A', 'R', 'T', 'Y'},
	};
	char words[15][11] = {
							"COMPUTER",
							"QUESTION",
							"CLARIFY",
							"NETWORK",
							"SYSTEM",
							"CLASS",
							"SEQUENCE",
							"CATCH",
							"MEMORY",
							"RANDOM",
							"ASSIGNMENT",
							"MARCH",
							"SCANT",
							"SPEED",
							"ENTER"
	};

	gridOut(grid);
	wordOut(words);

	cout << endl;
	find(grid, words);

	return 0;
}