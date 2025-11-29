// Ammar Ahmed		20L-0961		Home Work - I //

#include <iostream>
using namespace std;

void sumndAverageOfArray(int arr[], int size)
{
    int sum, average;
    sum = average = 0;

    for (int i = 0; i < size; i++)
    {
        if (arr[i] > 0)
            sum += arr[i];              // loop will go through each element and add to sum
           
    }
    average = sum / size;
    cout << "your sum " << sum << "\nyour average " << average << endl << endl;

}

void negativeOfArray(int arr[], int size)
{
       for (int i = 0; i < size; i++)
    {
        if (arr[i] < 0)
             cout << "negative values found in array";
            cout << arr[i] << "";
    }
}

void minimumOfArray(int arr[], int size)
{
    int v = arr[0];
    int index= 0;

    for (int i = 0; i < size; i++)
    {
        if (v > arr[i])
        {
            v = arr[i];
            index = i;
        }
    }
    cout << "\n\nminimum value of array " << v << " found at " << index << "th index";
}

int main()
{
    const int size = 6;
    int arr[size];
    
    cout << "Enter your elements" << endl;
    
    for (int i = 0; i < size; i++)  //array input
        cin >> arr[i];  

    sumndAverageOfArray(arr, size); //implementing Q4a
    negativeOfArray(arr, size);     //implementing Q4b
    minimumOfArray(arr, size);      //implementing Q4c and Q4d

    return 0;
}