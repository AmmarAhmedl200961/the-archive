#include <iostream>
#include <string>
using namespace std;

void out(string s1, string s2) {
	cout << "s1:" << s1 << endl;
	cout << "s2:" << s2 << endl;

}

int main() 
{
	string s1 = "FAST";
	string s2 = "University";

	cout << "Before Swapping:\n";
	out(s1, s2);

	// string is a seperate datatype than cstrings so I used swap for string function 
	//(https://en.cppreference.com/w/cpp/string/basic_string/swap)
	swap(s1, s2);

	cout << "After Swapping:\n";
	out(s1, s2);

	return 0;
}