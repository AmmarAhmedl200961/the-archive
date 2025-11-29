#include <iostream>
#include <fstream>
using namespace std;

#define maxdegree 200
#define maxpolynomials 10

struct polynomial
{
	int d;
	char vname;
	int CS[maxdegree]{};
};

void toLoadPolynomial(ifstream& Rdr, polynomial p)
{
	Rdr >> p.d;
	for (int ci = 0, i = p.d; ci <= p.d; ci++, i--)
	{
		int coef;
		Rdr >> coef;
		p.CS[i] = coef;
	}
}

void printPolynomial(const polynomial& p)
{
	for (int i = 0, ci = p.d; i <= p.d; i++, ci--)
	{
		if (p.CS[ci] != 0)
		{
			if (i != 0)
				cout << ((p.CS[ci] >= 0) ? "+" : "");
			
			cout << p.CS[ci];
			
			if (i != p.d)
			{
				if (i != p.d - 1)
					cout << "x^" << ci;
				else
					cout << "x";
			}
		}
	}
}

int MAX(int a, int b)
{
	return (a < b) ? b : a;
}

polynomial Add(const polynomial& p, const polynomial& s)
{
	polynomial R{};
	R.d = max(p.d, s.d);
	for (int i = 0; i <= R.d; i++) {
		R.CS[i] = p.CS[i] + s.CS[i];
	}
	return R;
}

void loadAllPolynomials(polynomial Ps[maxpolynomials], int& Psize)
{
	ifstream Rdr("record.txt");
	Rdr >> Psize;
	for (int pi = 0; pi < Psize; pi++) 
		toloadpolynomial(Rdr, Ps[pi]);
	
}
void printAllPolynomials(polynomial Ps[maxpolynomials], int Psize)
{
	system("cls");
	for (int pi = 0; pi < Psize; pi++)
	{
		printpolynomial(Ps[pi]);
		cout << "\n";
	}
}
polynomial multiplication(polynomial& xx, polynomial& yy)
{
	polynomial mul{ 1 };
	mul.d = max(xx.d, yy.d);

	for (int ma = 0; ma < xx.d; ma++)
	{
		for (int mb = 0; mb < yy.d; mb++)
		{
			mul.CS[ma + mb] += xx.CS[ma] * yy.CS[mb];
		}
	}

}
int main() {
	polynomial Ps[maxpolynomials]{};
	polynomial R;
	int Psize;
	loadAllPolynomials(Ps, Psize);
	printAllPolynomials(Ps, Psize);
	int ri, oli, ori;
	char opr;
	char dummy, tocontinue = 'Y';
	do
	{
		printallpolynomials(Ps, Psize);

		cin >> dummy >> ri >> dummy >> dummy >> oli >> opr >> dummy >> ori;
		switch (opr)
		{
		case'+':
			Ps[ri] = Add(Ps[oli], Ps[ori]);
			break;

		}
		printallpolynomials(Ps, Psize);
		cout << "do you want to continue>" << endl;
		cin >> tocontinue;
	}while (tocontinue == 'y' || tocontinue == 'Y');

	return 0;
}

