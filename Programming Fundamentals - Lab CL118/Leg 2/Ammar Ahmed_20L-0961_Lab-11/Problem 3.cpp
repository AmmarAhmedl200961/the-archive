#include <iostream>
#include <string>
using namespace std;

// Problem 3

//  Structs //

struct address
{
    int houseNo;
    string city;
    int pinCode;

};

struct employee
{
    int id;
    char name[20];
    float salary;
    
    address address;

};

//  Functions   //

void input(employee& a)
{
    cout << "Enter your Details: ";
    cout << "\nEnter ID: ";
    cin >> a.id;
    cout << "\nEnter Name: ";
    cin >> a.name[20];
    cout << "\nEnter Salary: ";
    cin >> a.salary;
    cout << "\nEnter HouseNo: ";
    cin >> a.address.houseNo;
    cout << "\nEnter your city: ";
    cin >> a.address.city;
    cout << "\nEnter the PinCode: ";
    cin >> a.address.pinCode;
}
void output(employee a)
{
    cout << endl;
    cout << "Entered details :\n";
    
    cout << "\nID: ";
    cout << a.id;
    cout << "\nName : ";
    cout << a.name;
    cout << "\nSalary : ";
    cout << a.salary;
    cout << "\nHouse no : ";
    cout << a.address.houseNo;
    cout << "\nCity : ";
    cout << a.address.city;
    cout << "\nPincode : ";
    cout << a.address.pinCode;
}
int main()
{

    employee emp;
    input(emp);
    output(emp);

    
    return 0;
}