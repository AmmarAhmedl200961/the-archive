#include <iostream>
#include <math.h>
using namespace std;

// i did not understand the "mostIntersecting" logic

void mostIntersecting(float X[], float Y[], float R[], int n)
{
	for (int i = 0; i < n-1; i++)
	{
		if (intersects(X, Y, R, i)==true)
		{
			cout << "Circle " << i << " intersects";
		}

	}
}


bool intersects(float X[], float Y[], float R[], int i)
{
	if ((X[i] - X[i + 1]) * (X[i] - X[i + 1]) + (Y[i] - Y[i + 1]) * (Y[i] - Y[i + 1]) <= (R[i] + R[i + 1]) * (R[i] + R[i + 1]))
		return true;
	else
		return false;
}

int main()
{
	cin.get();

	float X[10], Y[10], R[10];
	int n = 10;

	mostIntersecting(X, Y, R, n);



	return 0;
}