#include <iostream>
using namespace std;

 int main()
{
	int P1x, P2x, P1y, P2y, X, Y;
	cout << "Enter the coordinates for P1 : (x1, y1) : ";
	cin >> P1x >> P1y;
	cout << "Enter the coordinates for P2 : (x2, y2) : ";
	cin >> P2x >> P2y;
	cout << "Enter the coordinates of Point to which you want to check (X, Y): ";
	cin >> X , Y;
	if (P1y = P2y || P1x > X)
	{
		cout << "Point is on left side of the line segment.\n";
	}
	if (P1y = P2y && P2x < X)
	{
		cout << "Point is on right side of the line segment.\n";
	}
	if (P1y = P2y || P2x > X || P1x < X);
	{
		cout << "Point lies on the line segment.\n";
	}
	if (P1y < Y & P2y < Y)
	{
		cout << "Point lies above the line segment.\n";
	}
	if (P1y > Y || P2y > Y)
	{
		cout << "Point lies below the line segment.\n";
	}

	system("pause");
	return 0;
}