#include <iostream>

using namespace std;

int main()
{
    // Question 1
    
    string roll, batch, name, degmajor, crsTtl;
    char sec;
    int labNum;

    cout << "enter: roll, batch, name, degreemajor, course title, section and lab number";
    cin >>
        roll >> batch >> name >> degmajor >> crsTtl >> sec >> labNum;
    cout << "Welcome to " << crsTtl
          << "Name: " << name
        << "\nRoll #:" << batch << roll
        << "\nDegree:" << degmajor
        << "\nSection: " << sec
        << "\nLab: " << labNum;
		
	return 0;
}