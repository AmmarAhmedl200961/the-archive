#include <iostream>
#include <fstream>

using namespace std;

// Task 1
// Maam I have not covered file-handling to that extent, please mark leniently on this one as I tried my best.


const int rows = 13;
const int columns = 6;

char classType;
int rowNumber, Pcolumn;	//Pcolumn is our column position 
char column, choice;
char seats[rows][columns];

void showStatus();
void allocate();

int main()
{
	cout << "Program that organizes Airplane seating arrangement\n";

	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < columns; j++)
			seats[i][j] = '*';
	}

	do
	{
		showStatus();
		cout << endl;
		cout << "Enter type of Class\n";
		cout << "Enter (F or f) for First Class\n";
		cout << "Enter (B or b) for Business Class\n";
		cout << "Enter (E or e) for Economy Class\n";
		cin >> classType;

		switch (classType)
		{
		case 'F':
		case 'f':
		{
			cout << "enter row number -> 1 to 2";
			cin >> rowNumber;
			if (rowNumber == 1 || rowNumber == 2)
			{
				cout << "\nEnter Column -> A-F ";
				cin >> column;
				column = tolower(column);
				seatAllocate();
				showstatus();
			}
			else
				cout << "\ninvalid rown number for First class seat";

			break;
		}
		case 'B':
		case 'b':
		{
			cout << "enter row number -> 3 to 7";
			cin >> rowNumber;
			if (rowNumber == 3 || rowNumber == 4 || rowNumber == 5
				|| rowNumber == 6 || rowNumber == 7)
			{
				cout << "\nEnter Column -> A-F ";
				cin >> column;
				column = tolower(column);
				seatAllocate();
				showstatus();
			}
			else
				cout << "\ninvalid rown number for Business class seat";

			break;
		}
		case 'E':
		case 'e':
		{
			cout << "enter row number -> 8 to 13";
			cin >> rowNumber;
			if (rowNumber == 8 || rowNumber == 9 || rowNumber == 10
				|| rowNumber == 11 || rowNumber == 12
				|| rowNumber == 13)
			{
				cout << "\nEnter Column -> A-F ";
				cin >> column;
				column = tolower(column);
				seatAllocate();
				showstatus();
			}
			else
				cout << "\ninvalid rown number for Economy class seat";

			break;
		deafult:
			cout << "\nInvalid class type" << endl;
			exit(0);								// will exit the program
		}
		}
		cout << "\none more ticket to reserve (y/n)";
		
		cin >> choice;
	} while (tolower(choice) != 'n');

	return 0;
}

void showstatus()
{
	cout << "\n\tA\tB\tC\tD\tE\tF";
	for (int i = 0; i < rows; i++)
	{
		cout << "\n\tRow " << (i + 1);
		for (int j = 0; j < columns; j++)
			cout << "\t" << seats[i][j];

	}

}

void seatAllocate()
{
	Pcolumn = (tolower(column)) - 97;

	if (Pcolumn<0 || Pcolumn>columns)
	{
		cout << "invalid column\n";
		exit(0);
	}
	else
	{
		cout << "invalid column\n";
		exit(0);
	}
	else
	{
		if (seats[rowNumber][Pcolumn] == 'X')
		{
			cout << "ALready reserved, no vacancy";
		}
	}
	else
	{
	cout << "seat was reserved for you";
	}
	{
		for (int i = 0; i < rowNumber; i++)
		{
			for (int j = 0; j < Pcolumn; j++)
				seats[rowNumber - 1][Pcolumn] = 'X';
		}
	}


	
	
}
