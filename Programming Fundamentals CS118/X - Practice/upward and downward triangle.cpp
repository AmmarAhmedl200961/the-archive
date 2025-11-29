int height;
	cout << "Enter Height of Triangle => ";
	cin >> height;

	for (int i = 1; i <= height; i++)
	{
		for (int j = height - i; j > 0; j--)
		{
			cout << " ";
		}
		for (int k = 1; k <= i; k++)
		{
			cout << "* ";
		}
		cout << endl;
	}
	
	for (int i = height; i >= 1; i--)
	{
		for (int j = height - i; j > 0; j--)
		{
			cout << " ";
		}
		for (int k = i; k >= 1; k--)
		{
			cout << "* ";
		}
		cout << endl;
	}