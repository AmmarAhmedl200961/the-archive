#include <iostream>
using namespace std;

int main
{
	 // Question 7
    
    int marks;
    cout << "enter marks for grading scale:  ";
    cin >> marks;

    if (marks < 100 && marks > 90)
        cout << "Grade A+";
    else if (marks < 89 && marks > 80)
        cout << "Grade A";
    else if (marks < 79 && marks > 70)
        cout << "Grade B";
    else if (marks < 69 && marks > 60)
        cout << "Grade C";
    else if (marks < 59 && marks > 50)
        cout << "Grade D";
    else if (marks < 49 && marks > 00)
        cout << "Grade F";
    
	return 0;
}
	