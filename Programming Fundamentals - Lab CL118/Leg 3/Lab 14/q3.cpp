#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// change filename globally
string fname = "table.txt";

void outFile(int range) {
	int table = 2;

	fstream fout(fname, ios::out);

	for (int i = 1; i <= range; ++i) {
		fout << table << " * " << i << " = " << table * i << endl;
	}

	fout.close();
}

int main() 
{
	int range;
	cout << "Enter range ";
	cin >> range;

	outFile(range);

	return 0;
}