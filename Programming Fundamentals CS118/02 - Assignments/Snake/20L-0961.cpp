#include <windows.h>
#include <iostream>
#include <time.h>
using namespace std;

#include<conio.h>
#include<math.h>

void getRowColbyLeftClick(int& rpos, int& cpos)
{
	HANDLE hInput = GetStdHandle(STD_INPUT_HANDLE);
	DWORD Events;
	INPUT_RECORD InputRecord;
	SetConsoleMode(hInput, ENABLE_PROCESSED_INPUT | ENABLE_MOUSE_INPUT | ENABLE_EXTENDED_FLAGS);
	do
	{
		ReadConsoleInput(hInput, &InputRecord, 1, &Events);
		if (InputRecord.Event.MouseEvent.dwButtonState == FROM_LEFT_1ST_BUTTON_PRESSED)
		{
			cpos = InputRecord.Event.MouseEvent.dwMousePosition.X;
			rpos = InputRecord.Event.MouseEvent.dwMousePosition.Y;
			break;
		}
	} while (true);
}
void gotoRowCol(int rpos, int cpos)
{
	COORD scrn;
	HANDLE hOuput = GetStdHandle(STD_OUTPUT_HANDLE);
	scrn.X = cpos;
	scrn.Y = rpos;
	SetConsoleCursorPosition(hOuput, scrn);
}

struct Position
{
	int r, c;
};

struct Snake
{
	int Size;
	Position* Ps;

	char Sym;
	int color;
	int DIRECTION;

	int LeftKey;
	int RightKey;
	int DownKey;
	int UpKey;
};

#define ROW 80
#define COL 80
#define UP 1
#define DOWN 2
#define LEFT 3
#define RIGHT 4

#define UPKey 72
#define DOWNKey 80
#define LEFTKey 75
#define RIGHTKey 77

bool ValidFoodPosition(Snake S, Position FPOsition)
{
	for (int pi = 0; pi < S.Size; pi++)
		if (FPOsition.r == S.Ps[pi].r && FPOsition.c == S.Ps[pi].c)
			return false;
	return true;
}

void FoodGenerator(Position & FPOsition, Snake S)
{
	do
	{
		FPOsition.r = rand() % ROW;
		FPOsition.c = rand() % COL;
	} while (ValidFoodPosition(S, FPOsition));
}

void FoodDisplay(Position& FPOsition)
{
	char fsym = -37;
	gotoRowCol(FPOsition.r, FPOsition.c);
	cout << fsym;
}

void Init(Snake& S, Position &FPOsition)
{
	S.Size = 3;
	S.Ps = new Position[S.Size];
	S.Sym = -37;
	S.Ps[0].r = ROW	/ 2;
	S.Ps[0].c = COL / 2;

	S.Ps[1].r = ROW / 2;
	S.Ps[1].c = COL / 2-1;

	S.Ps[2].r = ROW / 2;
	S.Ps[2].c = COL / 2-2;
	S.DownKey = DOWNKey;
	S.UpKey = UPKey;
	S.LeftKey = LEFTKey;
	S.RightKey = RIGHTKey;
	S.DIRECTION = UP;

	FoodGenerator(FPOsition, S);

}

void DisplaySnake(Snake S, char sym)
{
	for (int startI = 0; startI < S.Size; startI++)
	{
		gotoRowCol(S.Ps[startI].r, S.Ps[startI].c);
		cout << sym;
	}
	gotoRowCol(S.Ps[0].r, S.Ps[0].c);
}

void SnakeMove(Snake& S)
{
	for (int positionI = S.Size - 1; positionI > 0; positionI--)
		S.Ps[positionI] = S.Ps[positionI - 1];

	switch (S.DIRECTION)
	{
	case UP:
		S.Ps[0].r--;
		if (S.Ps[0].r == -1)
			S.Ps[0].r = ROW - 1;
		break;
	case DOWN:
		S.Ps[0].r++;
		if (S.Ps[0].r == ROW)
			S.Ps[0].r = 0;
		break;
	case LEFT:
		S.Ps[0].c--;
		if (S.Ps[0].c == -1)
			S.Ps[0].c = COL - 1;
		break;
	case RIGHT:
		S.Ps[0].c++;
		if (S.Ps[0].c == COL)
			S.Ps[0].c = 0;
		break;
	}
}

bool GAMEOVER(Snake S)
{
	for (int startingI = 1; startingI < S.Size; startingI++)
	{
		if (S.Ps[0].r == S.Ps[startingI].r && S.Ps[0].c == S.Ps[startingI].c)
			return true;
	}
}

bool FoodCapture(Snake S, Position FPOsition)
{
	return S.Ps[0].r == FPOsition.r && S.Ps[0].c == FPOsition.c;
}

void ExtendSnake(Snake& S, Position TPOsition)
{
	Position* HPs = new Position[S.Size + 1];
	for (int pi = 0; pi < S.Size; pi++)
	{
		HPs[pi] = S.Ps[pi];
	}
	HPs[S.Size] = TPOsition;
	delete[]S.Ps;
	S.Ps = HPs;
	S.Size++;
}

int main()
{
	srand(time(0));
	int KeyVal=0;
	Position FPOsition;
	Position TPOsition;
	int Key;

	Snake S;
	Init(S, FPOsition);

	do
	{
		FoodDisplay(FPOsition);
		TPOsition = S.Ps[S.Size - 1];
		DisplaySnake(S, S.Sym);
		if (_kbhit())
		{
			KeyVal = _getch();

			if (S.LeftKey == KeyVal && S.DIRECTION != RIGHT)
				S.DIRECTION = LEFT;
			else if (S.RightKey == KeyVal && S.DIRECTION != LEFT)
				S.DIRECTION = RIGHT;
			else if (S.DownKey == KeyVal && S.DIRECTION != UP)
				S.DIRECTION = DOWN;
			else if (S.UpKey == KeyVal && S.DIRECTION != DOWN)
				S.DIRECTION = UP;

		}

		Sleep(100);
		DisplaySnake(S, ' ');
		SnakeMove(S);
		if (FoodCapture(S, FPOsition))
		{	
			ExtendSnake(S, TPOsition);
			FoodGenerator(FPOsition, S);
		}
	} while (!GAMEOVER(S));

	
	return 0;
}