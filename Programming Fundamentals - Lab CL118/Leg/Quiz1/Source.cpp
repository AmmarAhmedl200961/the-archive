#include <iostream>
using namespace std;

int main()
{
	cout << "enter a set of even or odd numbers";
	int i=0;
	int evenCount=0;
	int oddCount=0;


	while (i != -1)
	{
	
		cin >> i;
		
		if (i == -1)
			break;
		if (i % 2 == 0)
			evenCount += 1;
		else 

			oddCount += 1;
		
		
		
	}
	
	cout << evenCount<<endl;
	cout << oddCount;
	return 0;
}