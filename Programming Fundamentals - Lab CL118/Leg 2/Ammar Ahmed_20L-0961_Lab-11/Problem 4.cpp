#include <iostream>
using namespace std;

// Problem 4

//  Structs //

struct employee
{
    int id;
    char name[20];
    float salary;

};

//  Functions   //

employee input(employee a)
{
    cout << "\n Enter your Details: ";
    cout << "\nEnter ID: ";
    cin >> a.id;
    cout << "\nEnter name: ";
    cin >> a.name[20];
    cout << "\nEnter salary: ";
    cin >> a.salary;
    return a;

}


void SWAP(employee& e1, employee& e2, employee& e3, employee& e4, employee& temp1, employee& temp2)
{
    temp1 = input(e1);
    temp2 = input(e2);

    e2 = temp1;         // e1 is now e2
    temp1 = input(e3);

    e3 = temp2;         // e2 is now e3
    temp2 = input(e4);

    e4 = temp1;         // e3 is now e4
    e1 = temp2;         // e4 is now e1

}

void output(employee a)
{
    cout << "\nID: ";
    cout << a.id;
    cout << "\nName : ";
    cout << a.name;
    cout << "\nSalary : ";
    cout << a.salary;

}

int main()
{
    employee e1, e2, e3, e3, temp1, temp2;  // Temp1 and Temp2 will be used for swapping

    SWAP(e1, e2, e3, e3, temp1, temp2);
    
    cout << "\n Data of Employee 1 after swap: \n";
    output(e1);

    cout << "\n Data of Employee 2 after swap: \n";
    output(e2);

    cout << "\n Data of Employee 3 after swap: \n";
    output(e3);

    cout << "\n Data of Employee 4 after swap: \n";
    output(e3);

    
    return 0;
}