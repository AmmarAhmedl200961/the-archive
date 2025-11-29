#include <iostream>  
using namespace std;  

void PrintPattern(int size)
{
	char sp=' ';

	for(int i=1;i<=size;i++)    
	{    
		for(int j=1;j<=size-i;j++)    
		{    
			cout<<sp;    
		}    
		for(int up=1;up<=i;up++)    
		{    
			cout<<up;    
		}    
		for(int down=i-1;down>=1;down--)    
		{    
		cout<<down;    
		}    
	
		cout<<endl;    
	}    
}

int main()  
{  
int size;    
cout<<"Enter Size"<<endl;    
cin>>size;    
PrintPattern(size);

system("pause");
return 0;  
}  