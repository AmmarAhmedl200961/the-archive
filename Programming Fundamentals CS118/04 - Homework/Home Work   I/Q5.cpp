// Ammar Ahmed		20L-0961		Home Work - 1 //

#include <iostream>
using namespace std;

void displaymenu()
{
    system("cls");
    cout << "-1-Mean\n";
    cout << "-2-Median\n";
    cout << "-3-Mode\n";

}

void meanOfArray(int arr[], int size)
{
    int sum, average;
    sum = average = 0;

    for (int i = 0; i < size; i++)
    {
        if (arr[i] > 0)
            sum += arr[i];              //loop will go through each element and add to sum

    }
    average = sum / size;
    cout << "Your mean(average) value is " << average;

}

void medianOfArray(int arr[], int size)
{
	cout << "your median(middle) value is ";
	for (int i = 0; i < size; i++)		//applying ascending sort
	{
		for (int j = i + 1; j < size; j++)
		{
			int v = 0;
			if (arr[i] > arr[j])
			{
				v = arr[i];
				arr[i] = arr[j];
				arr[j] = v;
			}
		}
	}
	
	if (size % 2 != 0)					//a check for even sized mean
		cout << (double)arr[size / 2];
	cout << (double)(arr[(size - 1) / 2] + arr[size / 2]) / 2.0;
										//{ (n-1)/2 + (n/2) } /2, standard mean calculation
}

void modeOfArray(int arr[], int size)
{
	for (int i = 0; i < size; i++)		//applying ascending sort
	{
		for (int j = i + 1; j < size; j++)
		{
			int v = 0;
			if (arr[i] > arr[j])
			{
				v = arr[i];
				arr[i] = arr[j];
				arr[j] = v;
			}
		}
	}

										//storing the largest number to max
	int max;
	for (int i = 1; i < size; ++i)
		if (arr[0] < arr[i]) 
			max = arr[i];
	
	int t = max + 1;
	int count[t];						//count will will be max+1, I do not remember how to from this part onwards, as we did not do mode in class.
	for (int i = 0; i < t; i++)
		count[i] = 0;
									
	for (int i = 0; i < size; i++)		//will store count of each element, into input array
		count[arr[i]]++;

	int mode = 0;						//mode will be the index with maximum count
	int k = count[0];
	for (int i = 1; i < t; i++)
		if (count[i] > k)
		{
			k = count[i];
			mode = i;
		}
	
	cout << "your mode(most occuring) value is " << mode;
	
}


int main()
{
    const int size = 20;
    int arr[size];
    srand(time(NULL));
	for (int i = 0; i < size; i++)		//fills in 20 times while,
		arr[i] = rand() % 90 + 10;		// is in the range 10 to 90
    
    cout << "Initialised Array: ";      //array output
    for (int i = 0; i < 10; i++)
        cout << arr[i] << " ";
        
    cout << endl;
    
	int option;
	char tocontinue = 'Y';
	while (tocontinue == 'y' || tocontinue == 'Y')
	{
		displaymenu();
		cin >> option;
		switch (option)
		{
		case 1:
			meanOfArray(arr, size);
			cout << endl << endl;
			break;
		case 2:
			medianOfArray(arr, size);
			cout << endl << endl;
			break;
		case 3:
			modeOfArray(arr, size);
			cout << endl << endl;
			break;
		

		}

		cout << "\n\n Do you want to continue ? (Y/y)";
		cin >> tocontinue;
	}


    return 0;
}