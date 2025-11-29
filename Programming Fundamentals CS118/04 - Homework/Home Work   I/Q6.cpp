// Ammar Ahmed		20L-0961		Home Work - I //

#include <iostream>
using namespace std;

int main()
{
    int arr[10], int n;

    srand(time(0));                 //srand will generate random number every time
    for (int i = 0; i < 10; i++)
        arr[i] = rand() % 100 + 1;  //range will be form 1 to 100 to initialise in an array
    
    cout << "Initialised Array: ";  //array output
    for (int i = 0; i < 10; i++)
        cout << arr[i] << " ";
    
    cout << "\nEnter number to search between 1 and 100: ";
    cin >> n;
    for (int i = 0; i < 10; i++)
        if (arr[i] == n)            //searches for said occurence
        {
            cout << n << " is at " << i << "th index of array." << endl;
            break;
        }
    
    cout << "Element not found" << endl;
    return 0;
}