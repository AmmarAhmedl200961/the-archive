// Ammar Ahmed		20L-0961		Assignment 1 //

#include <iostream>
using namespace std;

int main()
{
	// first program
	int a = 1, b = 2;
	cout << "before swapping: " << " a " << a << " b " << b << endl;

	a = a + b;	// a = 3 temporarily
	b = a - b;	// b = 1, it has now been swapped with latter
	a = a - b;	// a = 2, it has now been swapped with latter

	cout << "after swapping: " << " a " << a << " b " << b << endl;

	// second program, will not work if one variable is a zero

	int c = 3, d = 4;

	cout << "before swapping: " << " c " << c << " d " << d << endl;
	
	c = c * d;	// c = 12 temporarily
	d = c / d;	// d = 3, it has now been swapped with latter
	c = c / d;	// c = 4, it has now been swapped with latter
	
	cout << "after swapping: " << " c " << c << " d " << d << endl;

	return 0;

	/* We can see that both solutions involve switching respective operators, operands have not been swiched. */
}