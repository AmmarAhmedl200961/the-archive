// Ammar Ahmed		20L-0961		Home Work - II //

#include <iostream> 
using namespace std;

int main() 
{
	int num, frst = 0, scnd = 0;

	cout << "The program finds the two largest integers in a list.";
	cout <<"\nEnter values, one per line, using a 0 to signal the end of the list." << endl << endl;
	
	int i = 0;

	while (true)			// Since 0 has to be entered in runtime, we can use infinite loop
	{
		cout << "? ";
		cin >> num;
		if (num == 0)		// 0 will end the input as a result
			break;
		if (i == 0) 
		{
			frst = num;
			scnd = num;		// initializing with user input in first run
		}
		else 
		{
			if (num >= frst)
			{
				scnd = frst; 
				frst = num;
			}
			
			else if (num > scnd && num != frst)
				scnd = num;

		} 

		i++;

	}
	cout << "\nThe Largest value is " << frst << endl; 
	cout << "The second largest value is " << scnd << endl;
	
	return 0;
}