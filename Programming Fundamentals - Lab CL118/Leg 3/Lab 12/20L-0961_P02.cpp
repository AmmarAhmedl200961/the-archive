#include <iostream>
using namespace std;

struct Student
{
	string name;
	int roll;
	int marks;
};

int main()
{
	Student d[5];

	// Input loop
	for (int i = 0; i < 5; i++)
	{
		cout << "Enter Data of " << i + 1 << " Student" << endl;
		cout << "Name ";
		cin >> d[i].name;
		cout << "Roll No. ";
		cin >> d[i].roll;
		cout << "Marks ";
		cin >> d[i].marks;
	}

	cout << endl << endl;


	// Output loop
	for (int i = 0; i < 5; i++)
	{
		cout << "Student " << i + 1 << endl;
		cout << "Name ";
		cout << d[i].name << endl;
		cout << "Roll No. ";
		cout << d[i].roll << endl;
		cout << "Marks ";
		cout << d[i].marks << endl;
	}

	return 0;
}