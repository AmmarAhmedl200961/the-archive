#include <iostream>  
using namespace std;  

void FindNumbers(int arr[],int size, int sum, int multiplication)
{
	for(int i=0;i<size;i++)
	{
		for(int j=i+1;j<size;j++)
		{
			if(arr[i]*arr[j]==multiplication)
			{
				if(arr[i]+arr[j]==sum)
				{
					cout<<"Numbers are "<<arr[i]<<" , "<<arr[j]<<". Their sum is "<<sum<<" and multiplication is "<<multiplication<<" ."<<endl;
				}
			}
		}
	}
}

int main()  
{  
	int arr[10]={1,5,6,7,8,9,4,11,12,3};
	int sum=9;
	int multiplication=18;

	FindNumbers(arr,10,sum,multiplication);

	system("pause");
	return 0;  
}  