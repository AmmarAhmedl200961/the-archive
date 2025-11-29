#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// Change wordlist size and textfile name here as global variables
const int wordlistC = 10;
string wordlist[wordlistC];
string fname = "dictionary.txt";

void infile()
{
	fstream fin(fname, ios::in);

	if (fin)
	{
		int i = 0;
		while (!fin.eof())
		{
			fin >> wordlist[i];
			++i;
		}
	}
	else
		cout << "Invalid or missing file";
	

	fin.close();
}

void outfile(string str_to_enter)
{
	fstream fout(fname, ios::app);

	if (fout)
		fout << endl << str_to_enter;
	else
		cout << "Invalid or missing file";

	fout.close();
}

void search(string in)
{
	// change caps of first letter of query to upper
	in.at(0) = toupper(in.at(0));

	for (int i = 0; i < wordlistC; i++)
	{

		
		
		if (in == wordlist[i])
		{
			cout << endl << "You Spelled Correctly";
			break;
		}
		else if (in < wordlist[i] && in.length() < wordlist[i].length())
		{
			cout << endl << "Did you mean \"" << wordlist[i] << "\" ?";
			break;

			// additional case of nextword in txt file being equal
			if (in == wordlist[i])
				break;
		}
		else
		{
			cout << endl << "Word isn't spelled Correctly";

			char opt = ' ';
			cout << endl << "Add new word to dictinary ? (y/n) ";
			cin >> opt;

			if (opt == 'y' || opt == 'Y')
			{
				// change caps of first letter of query to upper
				in.at(0) = toupper(in.at(0));
				outfile(in);
				cout << endl << "New word added succesfully";
			}

			break;
		}
	}

}

int main() 
{

	string in;
	
	while (true)
	{
		infile();

		// input
		cout << "\n\nEnter a word ";
		cin >> in;

		search(in);

	}
	return 0;
}