#include <iostream>
using namespace std;

// Problem 2

struct student
{
	char name[20];
	int roll;
	double marks;
};

int main()
{
	struct student stud[5];

	cout << "Enter name, roll and marks respectively\n";

	for (int i = 0; i < 5; i++)
	{
		cout << "Enter data of " << i << "st student";
		cout << "\nName: ";
		cin >> stud[i].name;
		cout << "\nRoll No: ";
		cin >> stud[i].roll;
		cout << "\nName: ";
		cin >> stud[i].marks;
	}

	for (int j = 0; j < 5; j++)
	{
		cout << "Student " << j;
		cout << "\nName: ";
		cout << stud[j].name;
		cout << "\nRoll No: ";
		cout << stud[j].roll;
		cout << "\nName: ";
		cout << stud[j].marks;
	}

	return 0;
}