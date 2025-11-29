// Ammar Ahmed		20L-0961		Assignment 1 //

#include <iostream>
using namespace std;

int main()
{
	char option;
    cout << "Welcome to the World of Control Structures\n\n"
        << "   .  Press (A) to add two integers\n"
        << "   .  Press (S) to subtract two integers\n"
        << "   .  Press (M) to multiply two integers\n"
        << "   .  Press (E) to exit the program\n";

    cin >> option;
    
    int I1=0, I2=0; 

    switch (option)
    {
        // adding another case helps counter event of smaller case option

    case 'a':
    case 'A':
    {
        cout << "Enter two Integers to add" << endl;
        cin >> I1 >> I2;
        cout << "\nYour result " << I1 + I2;
        break;
    }

    case 's':
    case 'S':
    {
        cout << "Enter two Integers to subtract" << endl;
        cin >> I1 >> I2;
        cout << "\nYour result " << I1 - I2;   
    }
    
    case 'm':
    case 'M':
    {
        cout << "Enter two Integers to multiply" << endl;
        cin >> I1 >> I2;
        cout << "\nYour result " << I1 * I2;
    }

    case 'e':
    case 'E':
        cout << "Exiting..." << endl;
        break;
  
    default:
        cout << "You have input an invalid command..." << endl;
        break;
    }
    
	return 0;
}