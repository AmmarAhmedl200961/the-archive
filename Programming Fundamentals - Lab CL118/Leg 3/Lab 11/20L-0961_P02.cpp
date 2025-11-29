#include <iostream>  
using namespace std;

void linearSearch(int arr[], int size)
{
    int search, flag = 0;

    cout << "Enter seach element ";
    cin >> search;

    int count = 1;
    for (int i = 0; i < size; i++)
    {
        if (arr[i] == search)
        {
            cout << endl << search << "is found at index " << count << " in the array";
            break;
        }
        count++, flag++;
        if (flag == size)
        {
            cout << "search is not concluded, element not found ";
        }

    }

}


int main()
{
    int arr[50] = { 9,55,60,81,49,66,49,10 };

    linearSearch(arr, 7);
    
    
    return 0;
}