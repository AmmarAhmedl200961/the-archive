#include <iostream> 
#include <cstdlib>
#include <cstring>
using namespace std;

int main()
{

    // I have used strcmp and strcpy to sort 10 students

    char name[10][50], tname[10][50], temp[50];

    int i, j, n=5;



    cout << "Enter Student Names";



    for (i = 0; i < n; i++)
    {

        cin >> name[i];

        strcpy_s(tname[i], name[i]);

    }



    for (i = 0; i < n - 1; i++)

    {

        for (j = i + 1; j < n; j++)

        {

            if (strcmp(name[i], name[j]) > 0)

            {

                strcpy_s(temp, name[i]);

                strcpy_s(name[i], name[j]);

                strcpy_s(name[j], temp);

            }

        }

    }



    cout << "Students after sorting";

    for (i = 0; i < n; i++)

    {

        cout << name[i] << endl;

    }





    return 0;
}