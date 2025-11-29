// Ammar Ahmed		20L-0961		Assignment 1 //

#include <iostream>
using namespace std;

int main()
{
	int option;
    cout << "Geometry Calculator\n\n"
         << "  1. Calculate the Area of a Circle\n"
         << "  2. Calculate the Area of a Rectangle\n"
         << "  3. Calculate the Area of a Triangle\n"
         << "  4. Quit\n";
    
    cin >> option;

    // initialising variables of area etc. later in event of quit option

    if (option == 4)
    {
        cout << "Program ended...";
    }

    else if (option == 3)
    {
        double area, base, height;
        cout << "Enter Triangle base.. " << endl;
        cin >> base;
        cout << "\nEnter Triangle height.. " << endl;
        cin >> height;
        area = base * height * 0.5;
        cout << endl << "Your Traingle area is " << area;
    }

    else if (option == 2)
    {
        double area, length, width;
        cout << "Enter Rectangle length.. " << endl;
        cin >> length;
        cout << "\nEnter Rectangle width.. " << endl;
        cin >> width;
        area = length * width;
        cout << endl << "Your Rectangle area is " << area;

    }

    else if (option == 1)
    {
        double area, radius, pi = 3.14159;
        cout << "Enter Circle radius.. " << endl;
        cin >> radius;
        area = pi * (radius * radius);
        cout << endl <<"Your Circle area is " << area;
    }

	return 0;
}