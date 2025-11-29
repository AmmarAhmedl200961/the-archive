# include <iostream>

using namespace std;

#define BLACK 0
#define WHITE 1

void PrintSnakes(ri,ci,Snakes[][2],Nos,rDim,cDim)
{
	for(s=0;s<Nos;s++)
	{
		int ss= Snakes[3][0], se=Snakes[5][0];
		PrintBox(ri,ci,rDim,cDim,-37);
		PrintCenter(ri,ci,rDim,cDim,ss);
		PrintBox(ri,ci+cDim,rDim,cDim,-37);
		PrintAtCenter(ri,ci+cDim,rDim,cDim,se);
		ri=ri+rDim;
	}
}

int NumbertoBoxNo(int Num)
{
	if(((Num-1)/10)%2==0)
	{return Num;
	}
	else
	{
		rowSkip=((Num-1)/10)*10;
		int ci=10-(Num-1)%10;
		return rowSkip+ci;
	}
}

void init(char B[8][8], int &turn)
{
	Turn=0;
	for(int ri=1;ri<7;ri++)
	{
		for(int ci=0;ci<8;ci++)
		{
			if(ri==1)
				B[ri][ci]='P';
			else if(ri==6)
				B[ri][ci]='p';
			else
				B[ri][ci]='-';
		}
	}
}

void GRID()

void PrintBoard(char B[][])
{
	for(int ri=0;ri<7;ri+)
	{	for(int ci=0;ci<7;ci++)
			////
			cout<<B[ri][ci];
			
	}
	cout<<endl;
}

void AskforSelection(int &sri,int &sci)
{
	cin<<sri<<sci;
	sri--;
	sci--;
}

bool IsBlackPiece(char s, sym B)
{
	return 'A'<=sym && sym <='Z'
}

bool IsWhitePiece(char s, sym w)
{
	return 'a'<=sym && sym <= 'z';
}

bool IsValidSelection(char s, int Turn)
{
	if(Turn==BLACK)
		return IsBlackPiece(S);
	else
		return IsWhitePiece(S);
}

bool IsValidDest(char sym, int Turn)
{
	
}

void MakeMoveOnBoard(char B[][P],int sri,int sci,int dri,int dci)
{
	B[dri[dci]=B[sri][sci];
	B[sri][sci];
}

int main()
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