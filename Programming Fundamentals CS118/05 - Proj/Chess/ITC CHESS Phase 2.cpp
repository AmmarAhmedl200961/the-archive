#include <iostream>
#include <windows.h>

#include <conio.h>
#include <math.h>

using namespace std;

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
	} 
	while (true);
}

void gotoRowCol(int rpos, int cpos)
{
	COORD scrn;
	HANDLE hOuput = GetStdHandle(STD_OUTPUT_HANDLE);
	scrn.X = cpos;
	scrn.Y = rpos;
	SetConsoleCursorPosition(hOuput, scrn);
}

 ChangeColor(int color)
{
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleTextAttribute(hConsole, color);
}

int main()
{
	int color = 0;
	while (true)
	{
		int rpos, cpos;
		getRowColbyLeftClick(rpos, cpos);
		gotoRowCol(rpos, cpos);
		cout << "Hello World";
		ChangeColor(color++);
		color %= 256;
	}
	return 0;
}

// chess functions

Check(char B[][8],int turn)
{
	int Kri, Kci;
	CheckOppKingPos(B,Turn,& Kri,& Kci);
}

bool isCheckMate (bool KingLegal, int CheckOppKingPos)
{
	// we need to check if King is legal
	bool iCheckMate = false;
	if (!KingLegal)
		return false;
	
	// to check for 8 cells surrounding kings'
	CheckOppKingPos[8] = // {1,-1},{1,0},{1,1},{0,1},{-1,1},{-1,0},{-1,-1},{0,-1}
	GameFinish = iCheckMate;
	return iCheckMate;
}
// check will also be implemented into IllegalMove

bool isStaleMate (bool isLegalMove bool CheckOppKingPos)
{
	bool iStaleMate = false;
	
	if (isLegalMove && CheckOppKingPos == true)
	{
		GameFinish = iStaleMate;
		return isStaleMate;
	}
	
	return isStaleMate;
}