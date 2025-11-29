// Ammar Ahmed		20L-0961		Assignment 2, Question 1 //
#include <iostream>
using namespace std;

void maxTriplet(int arr[], int size)
{
    int sum, ret1, ret2, ret3;
    sum = ret1 = ret2 = ret3 = 0;

    // ret1 and consecutive variables are needed to return following index of max-triplet
    // sum is needed to compare resulting sum of triplets and stored as max triplet with following logic:

    for (int i = 0; i < size; i++)
    {
        int index1 = i, index2 = i + 1, index3 = i + 2;

        if (sum < arr[index1] + arr[index2] + arr[index3])
        {
            sum = arr[index1] + arr[index2] + arr[index3];
            ret1 = arr[index1], ret2 = arr[index2], ret3 = arr[index3];
        }
        
    }

    cout << "Max Triplet: " << sum << endl;
    cout << "Triplet Values: " << ret1 << " " << ret2 << " " << ret3;
}

int sumtokarr(int arr[], int k, int i)
{
    int sum = 0;
    for (int var = 1; var <= k; var++)
    {
        // benefit of using this function is that we can freely use the ith index withour issue of having it corrupted
        sum += arr[i];
        i++;
    }

    return sum;
}

void maxNtuplet(int arr[], int size, int tuplet)
{
    int max = 0;


    for (int i = 0; i < size; i++)
    {
        int sum = 0;

        // to ease the process of making n tuplet sums i have used a kth sum function
        sum = sumtokarr(arr, tuplet, i);

        if (sum > max)
        {
            max = sum;
        }
    }

    cout << "Max " << tuplet << "-tuplet: " << max;

}

int main()
{

    const int size = 10;

    int list[size] = { 3,4,5,3,6,3,2,9,1,2 };
    int list1[size] = { 6,-1,7,3,-6,9,8,-5,4,19 };
    int tuplet;

    // max triplet takes an array with its size as parameter
    maxTriplet(list, size);

    cout << endl << endl << "Enter N: ";
    cin >> tuplet;
    
    
    // using if statement in-case N is beyond array size
    if (tuplet < size)
    {
        maxNtuplet(list, size, tuplet);
    }

    else
    {
        cout << "Invalid value of N entered...";
    }

    return 0;
}