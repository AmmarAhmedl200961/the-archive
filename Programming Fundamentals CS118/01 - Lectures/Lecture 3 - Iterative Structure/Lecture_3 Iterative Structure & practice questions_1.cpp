//upside down alternating 1's and 0's printing

cout << 
cin >> i;

	while (i>0)
	{
		j = 0;
		while(j < i)
		{	
			if(j % 2 == 0)
			{
				cout << "1";
			}
			else
			{
				cout << "0";
			}
			j++;
		}
		cout << endl;
		i--;
	}
	
	return 0;
	
//diamond printing

int main()
{
	int s;
	cout << "Enter number of Stars  ";
	cin >> s;
	
	for (i = 1; i <= s; i++)			//lecturers note
	{
		for (j = 1; j <= s-1; j++)
			cout << "";
		for (k = 0; k <= 2*i; k++)
			cout << "*";
		cout << endl;					//till here it prints upper part
		
	}
	
	for (i = s; i >= 1; i--)			//lecturers note
	{
		for (j = 1; j <= s-1; j++)
			cout << "";
		for (k = 0; k <= 2*i-1; k++)
			cout << "*";
		cout << endl;					//till here it prints lower part
		
	}
	
	
	return 0;
}
