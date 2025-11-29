#include <iostream>
#include<time.h>
#define Capacity 100
using namespace std;
void init(char Board[][Capacity], int& dim, char Pname[2][30], char Psym[2], int& Turn, int& wc)
{
	cout << "Enter Dimension ";
	cin >> dim;
	cout << "Enter Win Count ";
	cin >> wc;
	for (int i = 0; i < 2; i++)
	{
		cout << "Enter player" << i + 1 << "'s name: ";
		cin >> Pname[i];
	}
	for (int i = 0; i < 2; i++)
	{
		cout << "Enter player" << i + 1 << "'s symbol: ";
		cin >> Psym[i];
	}
	for (int ri = 0; ri < dim; ri++)
	{
		for (int ci = 0; ci < dim; ci++)
		{
			Board[ri][ci] = '-';
		}
	}
	Turn = rand() % 2;
}
void PrintBoard(char Board[][Capacity], int dim)
{
	system("cls");
	for (int ri = 0; ri < dim; ri++)
	{
		for (int ci = 0; ci < dim; ci++)
		{
			cout << Board[ri][ci] << "   ";
		}
		cout << endl;
	}
}
void UserInput(int& ri, int& ci, char Pname[], char Psym)
{
	cout << Pname << " Enter row index and coloumn index you want to place your character ' " << Psym << " '" << endl;
	cin >> ri;
	cin >> ci;
	ri--;
	ci--;
}
bool ValidInput(int ri, int ci, char Board[][Capacity], int dim)
{
	return ((ri >= 0 && ci >= 0) && (ri <= dim && ci <= dim) && Board[ri][ci] == '-');
}
void UpdateBoard(char Board[][Capacity], int  dim, int ri, int ci, char Psym)
{
	Board[ri][ci] = Psym;
}
bool HorizontalCheck(char Board[][Capacity], int dim, int wc, char Psym, int ri, int ci)
{
	if (ci + wc - 1 >= dim)
		return false;
	for (int i = 0; i < wc; i++)
	{
		if (Board[ri][ci + i] != Psym)
			return false;
	}
	return true;
}
bool VericalCheck(char Board[][Capacity], int dim, int wc, char Psym, int ri, int ci)
{
	if (ri + wc - 1 >= dim)
		return false;
	for (int i = 0; i < wc; i++)
	{
		if (Board[ri + i][ci] != Psym)
			return false;
	}
	return true;
}
bool RightDiagonalCheck(char Board[][Capacity], int dim, int wc, char Psym, int ri, int ci)
{
	if (ri + wc - 1 >= dim)
		return false;
	for (int i = 0; i < wc; i++)
	{
		if (Board[ri + i][ci + i] != Psym)
			return false;
	}
	return true;
}
bool LeftDiagonalCheck(char Board[][Capacity], int dim, int wc, char Psym, int ri, int ci)
{
	if (ci - (wc - 1) < 0)
		return false;
	for (int i = 0; i < wc; i++)
	{
		if (Board[ri + i][ci - i] != Psym)
			return false;
	}
	return true;

}
bool IsWin(char Board[][Capacity], int  dim, int wc, char Psym, int ri, int ci)
{
	bool Horizontal = HorizontalCheck(Board, dim, wc, Psym, ri, ci);
	bool Vertical = VericalCheck(Board, dim, wc, Psym, ri, ci);
	bool LeftDiagonal = LeftDiagonalCheck(Board, dim, wc, Psym, ri, ci);
	bool RightDiagnal = RightDiagonalCheck(Board, dim, wc, Psym, ri, ci);
	return (Horizontal || Vertical || LeftDiagonal || RightDiagnal);
}
bool IsDraw(char Board[][Capacity], int dim)
{
	for (int ri = 0; ri < dim; ri++)
	{
		for (int ci = 0; ci < dim; ci++)
		{
			if (Board[ri][ci] == '-')
				return true;
		}
	}
	return false;
}
void TurnChange(int& Turn)
{
	Turn = (Turn + 1) % 2;
}

void ComputerMove()
{
do 
{
	ri=rand(0-dim-1);
	ci=rand(0-dim-1);
}
while(Board[ri][ci] == '-')
  Psym=Board[ri][ci] == '-';
  for(ri=0;ri<dim;ri++)
  {
	  for(ci=0;ci<dim;ci++)
	  {
		  if(Board[ri][ci] == '-')
		  {
			  Board[ri][ci] == Turn;
			  if(IsWin(Turn))
			  {
				  Board[ri][ci] == '-';
				  Board[ri][ci] == Psym;
				  return;
			  }
			  else
			  Board[ri][ci] == '-';
		  }
	  }
  }
}

int main()
{
	srand(time(0));
	char Choice;
	char Board[Capacity][Capacity];
	char Pname[2][30];
	char Psym[2];
	int Turn, ri, ci, dim, wc;
	bool Gameover = false;
	int WinnerCount[2] = { '0' };
	int Winner = -1;
	do
	{
		init(Board, dim, Pname, Psym, Turn, wc);
		do
		{
			PrintBoard(Board, dim);

			do
			{
				UserInput(ri, ci, Pname[Turn], Psym[Turn]);
				if (!ValidInput(ri, ci, Board, dim))
				{
					cout << "Invalid input" << endl;

				}
			} while (!ValidInput(ri, ci, Board, dim));
			UpdateBoard(Board, dim, ri, ci, Psym[Turn]);
			for (int i = 0; i < dim; i++)
			{
				for (int r = 0; r < dim; r++)
				{
					Gameover = IsWin(Board, dim, wc, Psym[Turn], i, r);
					if (Gameover == true)
						break;
				}
				if (Gameover == true || i == dim - 1)
					break;
			}
			if (Gameover)
				Winner = Turn;
			if (!IsDraw(Board, dim))
				Gameover = true;
			if (!Gameover)
				TurnChange(Turn);
		} while (!Gameover);

		cout << endl;
		if (Winner == -1)
			cout << "Game has drawed!!!" << endl;

		else
		{
			cout << Pname[Turn] << "  has won!!!" << endl;
			WinnerCount[Winner]++;
		}

		cout << "Do you want to play again? y/n ";
		cin >> Choice;

	} while (Choice == 'y' || 'Y');

	for (int i = 0; i < 2; i++)
	{
		cout << "Player" << Pname[i] << " Has won " << WinnerCount[i] << " times";
	}
}