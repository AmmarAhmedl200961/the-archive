#include <iostream>
using namespace std;

// Problem 2

void rectangle(int h, int w)
{
	if (h <= 0 && w <= 0)
	{
		cout << "Rectangle printing is not possible.";
	}

	else
	{
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				cout << "O";
			}
			cout << endl;
		}
	}
}

int main()
{
	int height, width;
	cout << "Enter height and width ";
	cin >> height >> width;
	rectangle(height, width);

	return 0;
}