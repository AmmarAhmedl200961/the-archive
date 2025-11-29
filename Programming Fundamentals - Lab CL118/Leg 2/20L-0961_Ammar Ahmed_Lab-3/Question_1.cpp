#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    // Question 1

    int num;
    int table = 1;
    
    cout << "enter number to print table of  ";
    cin >> num;
    
    while (table <= 10)     //condition will stop exactly at 10
    {
        cout << num << " x " << table << " = " << num * table << endl;
        table++;
    }

    return 0;
}