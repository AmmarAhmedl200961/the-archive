#include <iostream>  
using namespace std;

void input(int arr[][50], int r, int c)
{
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < r; j++)
            cin >> arr[i][j];
    }
}

void output(int arr[][50], int r, int c)
{
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < r; j++)
            cout << arr[i][j] << " ";
        cout << endl;
    }
}
int main()
{
    int mat1[50][50], mat2[50][50], matans[50][50], r, c;

    cout << "Enter size of row:";
    cin >> r;

    cout << "Enter size of column:";
    cin >> c;


    cout << "Enter elements of Matrix A ";
    input(mat1, r, c);
    cout << "Enter elements of Matrix B ";
    input(mat2, r, c);
    
    // calculation
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
            matans[i][j] = mat1[i][j] - mat2[i][j];
    }

    cout << "A-B " << endl;
    output(matans, r, c);
    cout << endl;

	
	
	return 0;
}