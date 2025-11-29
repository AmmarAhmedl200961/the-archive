#include<iostream>
#include<iomanip>
#include<fstream>
using namespace std;

#define RCapacity 100
#define CCapacity 100

using namespace std;
void LoadData(int A[], int& Rows, int& Cols)
{
	ifstream Rdr("Test.txt");
	Rdr >> Rows,
		Rdr >> Cols;
	for (int ri = 0; ri < Rows; ri++)
	{
		for(int ci=0 ; ci<Cols ; ci++)
		{
			int d;
			Rdr >> d;
			A[ri][ci] = d;
		}
	}
}

void PrintMatrix(int A[][CCapacity], int Rows, int Cols)
{
	for (int ri = 0; ri < Rows; ri++)
	{
		for (int ci = 0; ci < Cols; ci++)
			cout << setw(3) << A[ri][ci];
		cout << "\n";
	}
}

int WindowSum(int D[][CCapacity], int sri, int sci, int WR, int WC)
{
	int sum = 0;
	for (int r = 0; r < WR; r++)
	{
		for (int c = 0; c < WC; c++)
		{
			sum += D[r + sri][c + sci];
		}
	}
	return sum;
}

void FindMax3by3Window(int D[][CCapacity], int rows, int cols, int& mri, int& mci, int& maxsum)
{
	maxsum = WindowSum(D, 0, 0, 3, 3);
	mri = 0, mci = 0;
	for (int ri = 0; ri < rows - 3; ri++)
	{
		for (int ci = 0; ci < cols - 3; ci++)
		{
			int sum = WindowSum(D, ri, ci, 3, 3);
			if (sum > maxsum);
			{
				mri = ri;
				mci = ci;
				maxsum = sum;
			}
		}
	}
}

bool addmatrix(int C[][CCapacity], int& CR, int& CC,
	int A[][CCapacity], int AR, int AC,
	int B[][CCapacity], int BR, int BC)
{
	if (AR != BR && AC != BC) {
		return false;
	}
	CR = AR;
	CC = AC;
	for (int ri = 0; ri < CR; ri++) {
		for (int ci = 0; ci < CC; ci++) {
			C[ri][ci] = A[ri][ci] + B[ri][ci];
		}
	}
	return true;
}
bool submatrix(int D[][CCapacity], int& DR, int& DC,
	int A[][CCapacity], int AR, int AC,
	int B[][CCapacity], int BR, int BC)
{
	if (AR != BR && AC != BC) {
		return false;
	}
	DR = AR;
	DC = AC;
	for (int ri = 0; ri < DR; ri++) {
		for (int ci = 0; ci < DC; ci++) {
			D[ri][ci] = A[ri][ci] - B[ri][ci];
		}
	}
	return true;
}

void loadmatrix(ifstream& Rdr, int M[RCapacity][CCapacity], int& rows, int& cols)
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

void printmatrix(int M[][CCapacity], int rows, int  cols)
{
	for (int ri = 0; ri < rows; ri++)
	{
		for (int ci = 0; ci < cols; ci++)
		{
			cout << M[ri][ci] << "\t";
		}
		cout << endl;
	}
}
int twodimensionintoone(int ri, int ci, int cols) {
	return (ri * cols) + ci;
}

void printmatrix(int M[], int R, int C)
{
	for (int ri = 0; ri < R; ri++) {
		for (int ci = 0; ci < C; ci++)
		{
			int x = twodimensionintoone(ri, ci, C);
			cout << setw(3) << M[x];
		}
		cout << endl;
	}
}
void TakingTranspose(int Transpose[RCapacity][CCapacity], int Matrix[RCapacity][CCapacity], int Rows, int Cols)
{
	for (int x = 0; x < Rows; ++x)
		for (int y = 0; y < Cols; ++y)
			Transpose[y][x] = Matrix[x][y];
}
int main_1()
{
	int Matrix[RCapacity][CCapacity];
	int Rows, Cols;
	int mri, mci, maxsum;
	LoadData(Matrix, Rows, Cols);
	PrintMatrix(Matrix, Rows, Cols);
	FindMax3by3Window(Matrix, Rows, Cols, mri, mci, maxsum);
	cout << "Max 3x3 window sum at " << mri << "  " << mci << endl;
	cout << "Sum is " << maxsum << endl;
	return 0;

}


int main_2() {

	ifstream Rdr("Data.txt");
	int A[RCapacity][CCapacity], rows1 = 5, cols1 = 3;
	int B[RCapacity][CCapacity], rows2 = 5, cols2 = 3;
	int C[RCapacity][CCapacity], CR, CC;

	loadmatrix(Rdr, A, rows1, cols1);
	loadmatrix(Rdr, B, rows2, cols2);

	printmatrix(A, rows1, cols1);
	cout << endl;
	printmatrix(B, rows2, cols2);

	if (addmatrix(C, CR, CC, A, rows1, cols1, B, rows2, cols2))
	{
		cout << "Sum of  a and b " << endl;
		printmatrix(C, CR, CC);
	}
	else
		cout << "order of matrix is change" << endl;


	int D[RCapacity][CCapacity], DR, DC;

	if (submatrix(D, DR, DC, A, rows1, cols1, B, rows2, cols2))
	{
		cout << "Subtraction is " << endl;

		printmatrix(D, DR, DC);
	}
	else
		cout << " matrixe do not match" << endl;
	return 0;
}

int main_5()
{
	int identity = 0;
	int Matrix[RCapacity][CCapacity], Rows, Cols;
	ifstream Rdr("Data4.txt");
	loadmatrix(Rdr, Matrix, Rows, Cols);
	if (Rows != Cols)
	{
		cout << "Matrix is not a square matrix";
		return 0;
	}
	for (int x = 0; x < Rows; x++)
		for (int y = 0; y < Cols; y++)
		{
			if ((Matrix[x][y] != 1) && (Matrix[y][x] != 0))
			{
				identity = 1;
				break;
			}
		}
	if (identity == 0)
		cout << "The given Matrix is an identity matrix.\n ";
	else
		cout << "The given Matrix is not an identity matrix.\n ";
	return 0;

}

int main_6()
{
	int Matrix[RCapacity][CCapacity], Rows, Cols;
	int Transpose[RCapacity][CCapacity];
	ifstream Rdr("Text1.txt");
	loadmatrix(Rdr, Matrix, Rows, Cols);
	int tRows = Cols, tCols = Rows;
	cout << "Your Matrix :" << endl;
	PrintMatrix(Matrix, Rows, Cols);
	TakingTranspose(Transpose, Matrix, Rows, Cols);
	cout << "It is a Transpose :" << endl;
	PrintMatrix(Transpose, tRows, tCols);
	return 0;
}