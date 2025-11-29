#include <iostream>
#include <cstdlib>
using namespace std;

void printArray(int [], int);
int primecheck (int);

void assignarray(int arr[],int size,int val)
{
	for(int i=0;i<size;i++)
	{
		arr[i] = val;
	}
}

int main()
{
	int arr[]={0};
	const int size =10;
	cout<<"Enter the number you want to put in array";
	for (int i=0;i<size;i++)
	{
		cin>>arr[];
	}
	
	//T enters the array

	system("pause");
	return 0;
}

int main_A_a()
{
	const int size =10;

	
	int zeroarr[size]={0}; 
	printArray(zeroarr, size);
	cout<<"\n";

	int Iarr[size];
	for (int i=0; i<size; i++)
	{
		Iarr[i]=i;
	}
	printArray(Iarr, size);
	cout<<"\n";

	int twoIarr[size];
	for (int i=0; i<size; i++)
	{
		twoIarr[i]=i*2;
	}
	printArray(twoIarr, size);
	cout<<"\n";

	int KIarr[size];
	for (int i=0; i<size; i++)
	{
		KIarr[i]=(size*i)+1;
	}
	printArray(KIarr, size);

	int primeArr[size];
	int k=0;
	for (int i=0; i<size; i++)
	{
		primeArr[i]=primecheck(i);
	}
	printArray(primeArr, size);
	
	int randomArray[size];
	for (int i = 0; i<size; i++)
      {
		  randomArray[i] = rand()%1000;
      }
	printArray(randomArray, size);


	system("pause");
	return 0;
}

int main_A_b()
{
	const int capacity=100;
	int A[capacity];
	int i;
	cout << "How many elements you want in an array ";
	int size;
	cin >> size;
	cout <<"What value you want to assign? ";
	cin>> i;
	assignarray(A,size,i);
	printarray(A,size);
	system("pause");
	return 0;
}

void printArray(int arr[], int k)
{
	for(int i=0; i<k; i++)
		cout<<arr[i]<<' ' ;
	
}

int primecheck(int a)
{
	int count=0;
	if (a==2)
		return a;
	for (int i=2;i<=a;i++)
	{
		if(a%i==0)
			count++;
	}
	if (count==1)
		return a;

}