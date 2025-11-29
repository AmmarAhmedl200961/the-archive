#include <iostream>
#include <string>
#include <fstream>
#include <bitset>
using namespace std;

char Reverse(string s1, string s2)
{
    cout << "Enter String 1" << endl;
    cin >> s1;
    cout << "Enter String 2" << endl;
    cin >> s2;

    if (s1.length() < s2.length())
    {
        cout << "String 2 is Larger";

        for (int i = s2.length() - 1; i >= 0; i--)
            return s2[i];

    }

    else
        {
        cout << "String 1 is Larger";
        for (int i = s1.length() - 1; i >= 0; i--)
                return s1[i];
        }
        

}

void wordCount()
{
    string words, fName;
    int iter=0;
    
    cout << "Enter your file Name\n";
    cin >> fName;
    
    ifstream file(fName);

    if (file)
    {
        while (!file.eof())
        {
            ++iter;
            file >> words;
        }

        cout << "words in " << fName << " are = " << iter;
    }
    else
        cout << "file not found\n";
    file.close();
}

void Random()
{
    int numbers;
    ofstream file;
    file.open("Random.txt");
    srand(time(0));

    if (file)
    {
        for (int i = 0; i < 50; i++)
        {
            numbers = rand() % 100 + 1;
            file << i << " " << numbers;
        }

        file.close();
    }
    else
        cout << "unable to open file";
}

void bitwise()
{
    int a[5], b[5];
    
    cout << "Enter elements of a, size 5\n";
    for (int i = 0; i < 5; i++)
        cin >> a[i];

    cout << "Enter elements of b, size 5\n";
    for (int i = 0; i < 5; i++)
        cin >> b[i];

    int AND, OR, XOR;
    XOR = AND = OR = 0; // Initialising

    for (int i = 0; i < 5; i++)
    {
        AND = a[5] & b[5];
        OR = a[5] | b[5];
        XOR = a[5] ^ b[5];
    }

    cout << "AND of the two arrays" << AND << "OR of the two arrays" << OR << "XOR of the two arrays" << XOR;
}

int main()
{
    // Task 1
    char s1, s2;
    string reverse(s1, s2);
    // Task 2
    wordCount();
    // Task 3
    Random();
    // Task 4
    bitwise();

    return 0;
}