#include <iostream>
using namespace std;

// Problem 3

void input(int arr_name[], int arr_size)
{
    for (int i = 0; i < arr_size; i++)
    {
        cin >> arr_name[i];
    }
}

void output(int arr_name[], int arr_size)
{
    for (int i = 0; i < arr_size; i++)
    {
        cout << arr_name[i] << " ";
    }

    cout << endl;
}

void findSubArr(int arr1[], int sub[], int size_arr1, int size_sub)
{
    int found = 0;

    for (int i = 0; i < size_arr1; i++)
    {
        for (int j = 0; j < size_sub; j++)
        {
            if (arr1[i] == sub[j])
            {
                found = i;
            }
        }
    }

    if (found > 0)
    {
        cout << "subarray exists from index " << found << " to " << found + size_sub;
    }

    else
    {
        cout << "no substring found";
    }

}

int main()
{
    int arr1[10], size1 = 10, sub_arr[3], size_sub = 3;
    
    cout << "enter array1[] values (non subarray) of size " << size1 << endl;
    input(arr1, size1);
    cout << "array1[] has values ";
    output(arr1, size1);
    cout << "enter array2[] values of size " << size_sub << endl;
    input(sub_arr, size_sub);
    
    findSubArr(arr1, sub_arr, size1, size_sub);


    return 0;
}