#include <iostream>
#include <math.h>

using namespace std;

bool isNorthSouthAxisMove(int sri,int sci,int eri,int eci)
{
	return (sci == sci);
}

bool isEastWestAxisMove(int sri, int sci, int eri, int eci)
{
	return(eri == sri)
		&&(sci != eci);
}

bool isSloppyAxisMove(int sri, int sci, int eri, int eci)
{
	int DelR = (eri - sri);
	int DelC = (eci - sci);
	
	/*return (DelR == DelC || DelR == -DelC);*/
	
	return (abs(DelR) == abs(DelC));	//using abs() approach form the math.h library
}

bool isNSPathClear(char B[][8], int sri, int sci, int eri, int eci)
{
	//using double loop in next code
	
	/*if (sri < eri)
	{
		for (int r = sri+1; r < eri; r++)
			if (B[r][sci] != '-')
				return false;
			
	}
	return true;
	else 
		for (int R = sri-1;R > eri;r--)
		{
			// //
		}
	return true;*/
	
	// using a single loop in next code
	
	int rs, re;
	if(sri < eri)
	{
		rs = sri+1;
		re = cri+1;
	}
	else
	{	
		rs = eri+1;
		re = sri-1; 
	}
	for (int r = rs; r <= re; r++)
	{	
		if(B[r][sci] != '-')
			return false;
	}
	return true;
}

bool isEastWestAxisPathClear( )
{
	
}

bool isSloppyMovePathClear(char B[][8], int sri, int sci, int eri, int eci)
{
	// we will use ∆r and ∆c, respectively known as DelR and DelC
	int DelR = eri - sri;
	int DelC = eci - sci;
	
	if (DelR > 0 && DelC < 0)
	{
		for (int i = 1; i < DelR; i++)
		{
			if(B[sri + i][sci - i] != '-')
				return false;
		}
	}
	return true;
}

bool isLegalMove (char B[][8], int sri, int sci, int eri, int eci)
{
	switch(B[sri][sci])
	{
		case 'R':
		case 'r':
			return RookLegal();
		case 'C':
		case 'c':
			return BishopLegal();
		case 'Q':
		case 'q':
			return QueenLegal();
		case 'K':
		case 'k':
			return KingLegal();
		case 'H':
		case 'h':
			return HorseLegal();
		case 'P'
			
		case 'p':
	}
}

bool RookLegal(char B[][8], int sri, int sci, int eri, int eci)
{
	bool (isNorthSouthAxisMove(sri,sci,eri,eci) && isNSPathClear(B,sri,sci,eri,eci))
			|| (isEastWestAxisMove(/ /) && isEastWestAxisPathClear(/ /))
}

bool BishopLegal(char B[][8], int sri, int sci, int eri, int eci)
{
	return (isSloppyAxisMove(B,sri,sci,eri,eci) && isSloppyMovePathClear(sri,sci,eri,eci));
}

bool QueenLegal(char B[][8], int sri, int sci, int eri, int eci)
{
	return (RookLegal(B,sri,sci,eri,eci) || BishopLegal(B,sri,sci,eri,eci));
}

bool KingLegal(char B[][8], int sri, int sci, int eri, int eci)
{
	////
}

bool HorseLegal(char B[][8], int sri, int sci, int eri, int eci)
{
	int DelR = abs(eri) - abs(sri);
	int DelC = abs(eci) - abs(sci);
	
	return (DelR == 1 && DelC == 2) || (DelR == 2 && DelC == 2);
}

void Higlight (B[][8], int eri, int eci)
{
	
}

int main() //partly form the phase 0 section of chess
{
	//some changes after phase 1 will be highlighted
	
	int turn;
	char B[8][8];
	int sri,sci
		dri,dci;
		
	init(B,Turn);
	cout<<Turn+1<<" 's Turn:  ";
	GRID(); //
	PrintBoard(B); //
	
	do
	{
		do
		{
			AskforSelection(sri,sci);
		
		}while(!IsValidSelection(sym, Turn))
		
		do
		{
			AskforDest(dri,dci);
			sym=B[dri][dci];
		
		}while(IsValidDest(eri, eci, B, Turn)) //
		
		if (isLegalMove(B, sri, sci, eri, eci))  //
		
		MakeMoveOnBoard(B,sri,sci,dri,dci);
		
		while(true)
		{
			WriteOnBoard(B, Sri, Sci, eri, eci); //
			PrintBoard(B); //
			TurnChange(Turn);
		}
	}
}