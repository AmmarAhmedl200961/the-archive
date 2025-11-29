#include <iostream>
using namespace std;

// Problem 5

void output(int arr_name[], int arr_size)
{
    for (int i = 0; i < arr_size; i++)
    {
        cout << arr_name[i] << " ";
    }

    cout << endl;
}

void init(int arr_name[], int arr_size)
{
    for (int i = 0; i < arr_size; i++)
    {
        arr_name[i] = 0;
    }
}


int main()
{
    int A[9];
    int size = 9;
    
    init(A, 9);
    cout << "Your Board " << endl;
    output(A, size);

    int u1, u2;
    cout << "enter position for starting USER 1 (0-8) ";
    cin >> u1;
    A[u1] = 1;
    output(A, 9);

    cout << endl;
    cout << "enter position for starting USER 2 (0-8) ";
    cin >> u2;
    A[u2] = 2;
    output(A, 9);

    while (true)
    {
        int left = 4, right = 6, input, userResult = 0;
        
        cout << "User 1 turn(Enter Move): (left<-4, 6-> right) [ 0 FOR NO MOVE ] ";
        cin >> input;

        if (input == left)
        {
            A[u1] = 0;
            userResult = 1;
            A[u1--] = userResult;
            output(A, 9);

        }
        else if (input = right)
        {
            A[u1] = 0;
            userResult = 1;
            A[u1++] = userResult;
            output(A, 9);

        }

        if (u1 == u2)
        {
            cout << "User " << userResult << " caught other User at location " << u1 << " User " << userResult << " won !!!";
            break;
        }

        cout << "User 2 turn(Enter Move): (left<-4, 6-> right) [ 0 FOR NO MOVE ] ";
        cin >> input;

        if (input == left)
        {
            A[u2] = 0;
            userResult = 2;
            A[u2--] = userResult;
            output(A, 9);

        }
        else if (input = right)
        {
            A[u2] = 0;
            userResult = 2;
            A[u2++] = userResult;
            output(A, 9);

        }

        if (u1 == u2)
        {
            cout << "User " << userResult << " caught other User at location " << u1 << " User " << userResult << " won !!!";
            break;
        }
        
    }


    return 0;
}