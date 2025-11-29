#include <iostream>
#include <conio.h>
using namespace std;

#define rows 127
#define cols 237

void initArray(char world[][cols], int r, int c, char LS)
{
	for (int ri = 0; ri < r; ri++)
	{
		for (int ci = 0; ci < c; ci++)
			world[ri][ci] = ' ';
		
	}

	for (int ci = 0; ci < c; ci++)
		world[r / 2][ci] = LS;
	
	for (int ri = 0; ri < r; ri++)
		world[ri][c / 2] = LS;
	
}

int neighborLivesCount(char world[][cols], int r, int c, int ri, int ci, char LS)
{
	int count = 0;
	for (int rii = ri - 1; rii <= ri + 1; rii++)
	{
		if (rii < 0 || rii == r)
			continue;
		for (int cii = ci - 1; cii <= ci + 1; cii++)
		{
			if (cii < 0 || cii == c)
				continue;
			if (rii == ri && cii == ci)
				continue;
			if (world[rii][cii] == LS)
				count++;
		}
	}
	return count;
}

void displayArray(char world[][cols], int r, int c)
{
	system("cls");
	for (int ri = 0; ri < r; ri++)
	{
		for (int ci = 0; ci < c; ci++)
			cout << world[ri][ci];
		
	}
}
void repopulate(char world[][cols], int r, int c, char LS)
{
	char theworld[rows][cols];
	for (int ri = 0; ri < r; ri++)
	{
		for (int ci = 0; ci < c; ci++)
		{
			int count = neighborlivescount(world, r, c, ri, ci, LS);
			if (world[ri][ci] == LS && count < 2)
				theworld[ri][ci] = ' ';
			
			else if (world[ri][ci] == LS && count >= 2 && count < 3)
				theworld[ri][ci] = world[ri][ci];
			
			else if (world[ri][ci] == LS && count > 3)
				theworld[ri][ci] = ' ';
			
			else if (world[ri][ci] == ' ' && count == 3)
				theworld[ri][ci] = LS;
			
			else
				theworld[ri][ci] = world[ri][ci];
			
		}
	}
	for (int ri = 0; ri < r; ri++)
	{
		for (int ci = 0; ci < c; ci++)
			world[ri][ci] = theworld[ri][ci];
		
	}
}
int main()
{
	_getch();
	
	char world[rows][cols];
	char sym = '*';

	initarray(world, rows, cols, sym);
	
	while(true)
	{
		displayarray(world, rows, cols);
		repopulate(world, rows, cols, sym);
	}
	
	return 0;
}