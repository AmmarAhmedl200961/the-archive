#include <iostream>
#include <fstream>
using namespace std;

#define Maxstudents 50

struct structstudent
{
	int rollno;
	char name[40];
	char gender;
	char fathersname[40];
	float grades;
};

void printStudent(const structstudent& s)
{
	cout << s.rollno << " " << s.name << " " << s.gender << s.fathersname << " " << s.grades << endl;
}

void readStudent(ifstream& Rdr, structstudent& s)
{
	Rdr >> s.rollno;
	Rdr.ignore();
	Rdr.getline(s.name, 50, '.');
	Rdr >> s.gender;
	Rdr.ignore();
	Rdr.getline(s.fathersname, 50, '.');
	Rdr >> s.grades;
}

void printStudents(structstudent Ss[], int SIZE)
{
	for (int i = 0; i < SIZE; i++)
		printstudent(Ss[i]);
	
}

void readStudents(structstudent Ss[], int& SIZE)
{
	ifstream Rdr("TEXT.txt");
	Rdr >> SIZE;
	for (int i = 0; i < SIZE; i++)
		readstudent(Rdr, Ss[i]);
	
}
int sortOutDictionary(char XX[], char YY[])
{
	int i;
	for (i = 0; XX[i] != '\0' && YY[i] != '\0'; i++) {
		if ((XX[i]) < (YY[i]))
			return -1;
		else if ((YY[i]) < (XX[i]))
			return 1;
	}
	if (XX[i] == '\0' && YY[i] != '\0')
		return -1;
	else if (YY[i] != '\0' && XX[i] != '\0')
		return 1;
	return 0;
}

void sortTheNames(structstudent Ss[], int size)
{
	int name;
	for (int n = 0; n < size; n++)
	{
		for (int i = 0; i + 1 < size; i++)
		{
			name = sortoutdictionary(Ss[i].name, Ss[i + 1].name);
			if (name == 1)
			{
				structstudent c = Ss[i];
				Ss[i] = Ss[i + 1];
				Ss[i + 1] = c;
			}
		}
	}
}

void sortGrades(structstudent Ss[], int SIZE)
{
	for (int x = 0; x < SIZE; x++)
		for (int gi = 0; gi + 1 < SIZE; gi++)
		{
			if (Ss[gi].grades < Ss[gi + 1].grades)
			{
				structstudent x = Ss[gi];
				Ss[gi] = Ss[gi + 1];
				Ss[gi + 1] = x;
			}
		}
}



int main()
{

	int SIZE;
	structstudent Ss[Maxstudents];
	readStudents(Ss, SIZE);
	cout << "before sorting the array is" << endl << endl;
	printStudents(Ss, SIZE);
	cout << "after sorting the new aray becomes" << endl;
	sortGrades(Ss, SIZE);
	printStudents(Ss, SIZE);
	return 0;
}
