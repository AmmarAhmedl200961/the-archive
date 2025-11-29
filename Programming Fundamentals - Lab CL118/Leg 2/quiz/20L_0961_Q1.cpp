#include <iostream> 
using namespace std; 

void mergeArrays(int A[], int B[], int size1, int size2)
{
	for (int i = 0; i < size1; i++)
	{
		if (A[i] > B[i])
			B[i] = A[i];
	}

}

void output(int arr[], int size)
{
	for (int i = 0; i < size; i++)
		cout << arr[i] << " ";
	

	cout << endl;
}

int main()
{
	cin.get();

	const int size1 = 3, size2 = 5;
	int A[size1] = { 10, 15, 25 };
	int B[size2] = { 1, 5, 20, 30 };  
	output(A, size1);
	output(B, size2);
	mergeArrays(A, B, size1, size2);
	cout << "The resulting arrays are : ";
	output(A, size1);  output(B, size2);
	
	return 0;
}
