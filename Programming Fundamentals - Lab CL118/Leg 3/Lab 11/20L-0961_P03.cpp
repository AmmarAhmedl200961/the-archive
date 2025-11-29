#include <iostream> 
#include <cstdlib>
using namespace std;

void linearSearch_2D(int arr1[][5], int arr2[][5])
{
    int count = 1, flag = 0, size = 2 * 5;

    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (arr1[i][j] == arr2[i][j])
            {
                flag++;
            }
            else
            {
                count++;
            }
        }
    }

    if (flag != size)
    {
        cout << "You lost the prize from " << count << " numbers";
    }

    else
    {
        cout << "YOU WON THE PRIZE";
    }
}

void init(int arr[][5])
{
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            int r = (rand() % 9) + 1;
            arr[i][j] = r;
        }
    }
}

void out(int arr[][5])
{
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
}

void in(int arr[][5])
{
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            cin >> arr[i][j];
        }
    }
}

int main()
{
    cin.get();

    int arr[2][5], arrIn[2][5];
    init(arr);
    cout << "Enter your Premium Bond number: ";
    in(arrIn);
    cout << "Premium Bond Prize Winner " << endl;
    out(arr);

    linearSearch_2D(arr, arrIn);
    
    
    return 0;
}