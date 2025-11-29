#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() 
{
	vector<int>g1(10);

	// populate a vector
	for (int i = 0; i < g1.size(); ++i)
		g1[i] = i;

	cout << "Normal iterator" << endl;

	// iterator
	for (auto i = g1.begin(); i != g1.end(); ++i) {
		cout << *i << " ";
	}

	cout << endl <<"Reverse iterator" << endl;

	// reverse iterator
	for (auto i = g1.rbegin(); i != g1.rend(); ++i) {
		cout << *i << " ";
	}

	return 0;
}