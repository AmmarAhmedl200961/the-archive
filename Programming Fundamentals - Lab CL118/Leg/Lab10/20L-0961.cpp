#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

#define RCapacity 100
#define CCapacity 100

void printMatrix(int A[][CCapacity], int Rows, int Cols)
{
	for (int ri = 0; ri < Rows; ri++)
	{
		for (int ci = 0; ci < Cols; ci++)
		{
			cout << setw(3) << A[ri][ci];
		}
		cout << endl;
	}
}
void loadMatrix(ifstream& Rdr, int M[RCapacity][CCapacity], int& rows, int& cols)
{
	Rdr >> rows >> cols;
	for (int ri = 0; ri < rows; ri++)
	{
		for (int ci = 0; ci < cols; ci++)
		{
			Rdr >> M[ri][ci];
		}
	}
}

bool rotateAntiClockwise90(int A[RCapacity][CCapacity], int Rows, int Cols, int n)
{
	int rotMatrix[RCapacity][CCapacity];
	bool firstSWAP = true;
	if (Rows != Cols)
		return false;
	for (n = n; n != 0; n--) 
	{
		for (int ri = 0; ri < Rows; ri++) 
		{
			for (int ci = 0; ci < Cols; ci++)
				rotMatrix[ri][ci] = A[Cols - ci - 1][ri];
			
		}

		for (int ri = 0; ri < Rows; ri++)
		{
			for (int ci = 0; ci < Cols; ci++) 
				A[ri][ci] = RotMatrix[Rows - 1 - ri][Cols - ci - 1];
		}
	}
	return true;
}

bool rotateClockwise90(int A[RCapacity][CCapacity], int Rows, int Cols, int n)
{
	int rotMatrix[RCapacity][CCapacity];
	bool firstSWAP = true;
	if (Rows != Cols)
		return false;
	for (n = n; n != 0; n--)
	{
		for (int ri = 0; ri < Rows; ri++) 
		{
			for (int ci = 0; ci < Cols; ci++)
				RotMatrix[ri][ci] = A[Cols - ci - 1][ri];
			
		}

		for (int ri = 0; ri < Rows; ri++) 
		{
			for (int ci = 0; ci < Cols; ci++) 
				A[ri][ci] = RotMatrix[ri][ci];
			
		}
	}
	return true;
}

int maxSummedRow(int Matrix[][CCapacity], int Rows, int Cols, int& MaxR)
{
	int Max, Sum = 0;
	for (int ci = 0; ci < Cols; ci++)
		Sum += Matrix[0][ci];
	
	MaxR = 0;
	Max = Sum;
	for (int ri = 1; ri < Rows; ri++)
	{
		Sum = 0;
		for (int ci = 0; ci < Cols; ci++)
			Sum += Matrix[ri][ci];
		
		if (Max < Sum)
			Max = Sum, MaxR = ri;
	}
	MaxR++;
	return Max;
}

int maxSummedCol(int Matrix[][CCapacity], int Rows, int Cols, int& MaxC)
{
	int Max, Sum = 0;
	for (int ri = 0; ri < Rows; ri++)
		Sum += Matrix[ri][0];
	
	MaxC = 0;
	Max = Sum;
	for (int ci = 1; ci < Cols; ci++)
	{
		Sum = 0;
		for (int ri = 0; ri < Rows; ri++)
			Sum += Matrix[ri][ci];
		
		if (Max < Sum)
			Max = Sum, MaxC = ci;
	}
	MaxC++;
	return Max;
}
bool isLowerTriangularMatrix(int mat[RCapacity][CCapacity], int rows, int cols)
{
	for (int i = 0; i < rows; i++)
		for (int j = i + 1; j < cols; j++)
			if (mat[i][j] != 0)
				return false;
	return true;
}
int main_CHALLANGE()
{
	ifstream Rdr("Text.txt");
	int A[RCapacity][CCapacity];
	int rows, cols, n=1;    // n is the multiple of 90 you want to rotate to i.e 1 for 90, 2 for 180, 3 for 270
	loadmatrix(Rdr, A, rows, cols);
	cout << "Orignal Matrix"<< endl;
	printMatrix(A, rows, cols);
	if (rotateClockwise90(A, rows, cols, n))
	{
		cout << "clockwise rotatation of the matrix at " << n << " degree is" << endl;
		printMatrix(A, rows, cols);
	}
	else
	{
		cout << "Rows not equal to cols";
	}
	ifstream fin("Text.txt");
	int M[RCapacity][CCapacity];
	loadmatrix(fin, M, rows, cols);
	cout << "anti clockwise rotatation of the matrix at " << n <<" degree will be" << endl;
	rotateAntiClockwise90(M,rows,cols,n);
	printMatrix(M, rows, cols);
	return 0;
}
int main_7() 
{
	ifstream Rdr("Data8.txt");
	int A[RCapacity][CCapacity];
	int rows, cols;
	int maxR, maxC;
	loadmatrix(Rdr, A, rows, cols);
	printMatrix(A, rows, cols); 
	cout << endl;
	cout << "Max sum of rows is ";
	cout << maxSummedRow(A, rows, cols,maxR) ;
	cout << endl;
	cout << " And the max summed row of the matrix is at index " << maxR;;
	cout << endl;
	cout << "max sum of col is ";
	cout << maxSummedCol(A, rows, cols,maxC);
	cout << endl;
	cout << "the max summed column is=" << maxC;
	cout << endl;
	return 0;
}


int main_8()
{
	int Matrix[RCapacity][CCapacity],rows,cols;
	ifstream Rdr("Data7.txt");
	loadmatrix(Rdr, Matrix, rows, cols);
	cout << "Matrix";
	printMatrix(Matrix, rows, cols);
	cout << endl;
	if (isLowerTriangularMatrix(Matrix,rows,cols))
		cout << "Yes it is lower triangular" << endl;
	else
		cout << "No it is not lower triangular"<<endl;
	return 0;
}
