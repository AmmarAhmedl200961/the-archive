#include <iostream>
using namespace std;

int main
{
	 // Question 4

    char alphabet;

    int lowerVowel, upperVowel; // checking vowels first and their counters eliminates need to check for consonants...

    cout << "Enter an alphabet: ";
    cin >> alphabet;

    lowerVowel = (alphabet == 'a' || alphabet == 'e' || alphabet == 'i' || alphabet == 'o' || alphabet == 'u');

    upperVowel = (alphabet == 'A' || alphabet == 'E' || alphabet == 'I' || alphabet == 'O' || alphabet == 'U');

    if (lowerVowel || upperVowel)
        cout << alphabet << " is a vowel.";
    else
        cout << alphabet << " it is not a vowel."; // lab instructor specified us to check for vowels only
   
    
	return 0;
}
	