#include <iostream>
using namespace std;

struct BooksS
{
	// title, author, and number_pages price,
	char title[10];
	char author[10];
	int number_pages;
	int price;
};

struct ShirtS
{
	// color, size, design price
	char color;
	char size[3];
	int design;
	int price;
};

union BookU
{
	// title, author, and number_pages price,
	char title[10];
	char author[10];
	int number_pages;
	int price;
};

union ShirtU
{
	// color, size, design price
	char color;
	char size[3];
	int design;
	int price;
};

int main()
{

	BooksS bs;
	BookU bu;
	ShirtS ss;
	ShirtU su;

	cout << "size of book struct " << sizeof(bs) << endl;
	cout << "size of book union " << sizeof(bu) << endl;
	cout << "size of shirt struct " << sizeof(ss) << endl;
	cout << "size of shirt union " << sizeof(su) << endl;






	return 0;
}