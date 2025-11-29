#include <iostream> 
#include <cstdlib>
using namespace std;

void linearSearch_2D(char arr1[][5], char arr2[][5])
{
    int score = 0;

    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (arr1[i][j] == arr2[i][j])
            {
                score++;
            }
        }
    }

    cout << endl;

    if (score >= 18)
        cout << "You got A grade ";
    else if (score >= 14)
        cout << "You got B grade ";
    else if (score >= 10)
        cout << "You got C grade ";
    else if (score < 10)
        cout << "FAIL";


}


void in(char arr[][5])
{

    int size = 1;
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            cout << size++ << ". ";
            cin >> arr[i][j];
            cout << endl;
        }
    }
}

int main()
{
    char arrAns[4][5] = { {'B','D','A','A','C'},{'A','B','A','C','D'} ,{'B','C','D','A','D'},{'C','C','B','D','A'} };
    char arrIn[4][5];

    cout << "Enter your answers " << endl;
    in(arrIn);

    linearSearch_2D(arrIn, arrAns);
    
    return 0;
}