// Ammar Ahmed		20L-0961		Assignment 1, Question 4 //
#include <iostream>
using namespace std;

int main()
{

    int in;
    cin >> in;

    if (in != 0 && in != 1) {
        cout << "Input is not binary";
    }

    while (in == 0 || in == 1)
    {
        // Check for 1-> 0-> 1-> 0-> 1
        if (in == 1) {
            cin >> in;
            if (in == 0) {
                cin >> in;
                if (in == 1) {
                    cin >> in;
                    if (in == 0) {
                        cin >> in;
                        if (in == 1) {
                            // If input is exact, loop is terminated with a prompt
                            cout << "Input terminated";
                            break;
                        }
                    }
                }
            }
        }

        // Nested loop check fails, then asks for input again
        cin >> in;

    }

    return 0;
}