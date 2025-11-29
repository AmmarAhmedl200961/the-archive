#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// change filename globally
string fname = "table.txt";

void inFile() {

	string line[20];

	fstream fin(fname, ios::in);

	if (fin.is_open()) {

		int i = 0;
		while (!fin.eof())
		{
			getline(fin, line[i]);
			++i;
		}

		for (int j = 0; j < i; j++)
			cout << line[j] << endl;

		fin.close();
	}
	else
		cout << endl <<"Invalid or missing file";
}

void outFile(int range) {
	int table = 3;

	fstream fout(fname, ios::app);

	fout << endl;

	for (int i = 1; i <= range; ++i) {
		fout << table << " * " << i << " = " << table * i << endl;
	}

	fout.close();
}

int main() 
{
	// reading file function
	inFile();

	// input the range and then append to file
	int range;
	cout << "Enter range ";
	cin >> range;

	outFile(range);

	return 0;
}