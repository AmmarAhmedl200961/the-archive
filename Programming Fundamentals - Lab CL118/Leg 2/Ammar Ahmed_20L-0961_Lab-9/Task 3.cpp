#include <iostream>
#include <fstream>

void display(int arr[][5]);

using namespace std;

// Task 3

const int rows = 5;
const int columns = 5;

void main()
{
	int firstMatrix[rows][columns], secondMatrix[rows][columns], resultMatrix[][];
	
	cout << "enter first matrix\n";
	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < columns; j++)
		{
			cout << "row number " << i << "column number " << j;
			cin >> firstMatrix[i][j];
		}
	}

	

	cout << "enter second matrix\n";
	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < columns; j++)
		{
			cout << "row number " << i << "column number " << j;
			cin >> secondMatrix[i][j];
		}
	}
    
    
    
    for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < columns; j++)
            for (int k = 0; k<2; k++)
            {
                resultMatrix[i][j] += firstMatrix[i][k] * secondMatrix[k][j];
            }
	}

    display(resultMatrix[][]);
}

void display(int arr[][5])
{
	ofstream fout;
	fout.open("matrix.txt");
	for (int i = 0; i < rows; i++)
		for (int j = 0; j < columns; j++)
			fout  << arr[i][j] << " ";
	fout.close();
}