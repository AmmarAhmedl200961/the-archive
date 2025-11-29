// Ammar Ahmed		20L-0961		Assignment 2, Question 2 //
#include <iostream>
using namespace std;

// functions
void reverse(int arr[], int size)
{
    int temp, start = 0, end = size - 1;
    while (start < end)
    {
        temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}

void bigIn(int arr[], int size)
{
    cout << "Enter bigInt: ";

    for (int i = 0; i < size; i++)
    {
        cin >> arr[i];
    }
}

void bigOut(int arr[], int size)
{
    for (int i = 0; i < size / 2; i++)
    {
        if (arr[i] == 0)
            continue;
        else
        {
            for (int j = i; j < size; j++)
                cout << arr[j];
        }

        break;
    }
}

void bigAdd(int arr1[], int arr2[], int arrAns[], int size) 
{
    int  k = size - 1, l = size - 2;
    int carry, sum, ans;
    carry = sum = ans = 0;
    for (; k != 0; --k, --l)
    {
        sum = arr1[l] + arr2[l] + carry;
        arrAns[k] = sum % 10;
        carry = sum / 10;
    }
    arrAns[k] = carry;
    k = size;

}
void bigDiff(int arr1[], int arr2[], int arrAns[], int size) 
{
    for (int index = size - 1; index >= 0; index--)
    {
        if (arr1[index] < arr2[index])
        {
            arr1[index] = arr1[index]--;
            arr1[index--] = arr1[index--] + 10;
        }
        arrAns[index] = arr1[index] - arr2[index];
    }
}


// Given Main function for question
int main() {
    const int size = 10;
    int big1[size];
    int big2[size];
    int big3[size + 1];
    int big4[size];

    cout << "Enter " << size << " digit long numbers\n";
    bigIn(big1, size);
    bigIn(big2, size);

    cout << "Big1: ";
    bigOut(big1, size);
    cout << endl;
    cout << "Big2: ";
    bigOut(big2, size);
    cout << endl;

    bigAdd(big1, big2, big3, size);
    cout << "Big1+Big2: ";
    bigOut(big3, size + 1);
    cout << endl;

    bigDiff(big1, big2, big4, size);
    cout << "Big1-Big2: ";
    bigOut(big4, size);
    cout << endl;

    return 0;
}
