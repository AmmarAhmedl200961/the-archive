#include <iostream>
using namespace std;

// Problem 4

void printPrime(int start, int end)
{
    cout << "Primes between " << start << " and " << end << endl;
    
    for (int j = start; j <= end; j++)
    {
        int i = 2;
        while (i <= j - 1)
        {
            if (j % i == 0)
                break;
            i++;
        }

        if (i == j && i != 2)
            cout << j << " ";
    }

}

int main()
{
	int n1, n2;
    cout << "enter prime numbers to find in: (start & end) ";
    cin >> n1 >> n2;
    printPrime(n1, n2);

	return 0;
}