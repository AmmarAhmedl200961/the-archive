#include <iostream>
using namespace std;

//For this task I had to search online for the techniques, some material is also ambiguous for me  
//Question 4

int main()
{
  int n,f = 0,sum = 0;	//f will be our final condition
  
  cout << "Enter a positive integer: ";
  cin >> n;
  int c = 1;
  
  while(sum < n)
  {
    sum = 0;
    for(int i = 1;i <= c;++i )	//we will be using progressive sum method
     sum +=i;
    
	if(sum == n) {f = 1; break;}
    c++;
  }

  if(f)
	  cout << "Triangle number" << endl;
  else 
	  cout << "Not a triangle number " << endl;
 
 return 0;
 
}