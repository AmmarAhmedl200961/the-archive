// Ammar Ahmed		20L-0961		Assignment 2 //

#include <iostream>
#include <string>
#include <map>
#include <fstream>
using namespace std;

// I am sorry that I had to use map, as map made super anagram function easier.


bool isSuperAnagram(string& first_word, string& second_word)
{
    int first_word_length = first_word.length();        // Finding Lengths 
    int second_word_length = second_word.length();

    map < char, int > alphabets;                        // A simple map container

    for (int i = 0; i < first_word_length; i++)
    {
        char ch = first_word[i];                        // ch is used as an index, for the map container
        
        if (alphabets.count(ch) == 1)
            alphabets[ch]++;
        
        else
            alphabets[ch] = 1;
        
    }

    for (int i = 0; i < second_word_length; i++)
    {
        char ch = second_word[i];
        
        if (alphabets.count(ch) == 1)
            alphabets[ch]--;
        
        else
            alphabets[ch] = -1;
        
    }

    int total_diff = 0;

    for (auto it = alphabets.begin(); it != alphabets.end(); ++it)
    {
        int value = it->second;
        
        if (value < 0)
            total_diff -= value;
        
        else
            total_diff += value;
        

    }


    return total_diff <= 2;                             // total_diff will be our ending condition as it suits the nature of super anagram        
}


bool isImpefectPalindrome(string& word)
{

    string reversed_word;
    int word_len = word.length();

    for (int i = word_len - 1; i >= 0; i--)
        reversed_word.push_back(word[i]);
    

    if (word == reversed_word)
        return false;
    

    int index = 0;
    int total_diff = 0;

    while (index < word_len)
    {
        if (word[index] != reversed_word[index])
            total_diff++;
     

        index++;
    }

    return total_diff <= 2;
}

void program()
{
    ifstream file;
    file.open("file.txt");
    string line;
    int line_num = 0;

    while (getline(file, line))
    {
        string s1;
        string s2;

        int index = 0;
        int line_len = line.length();

        bool isFirst = true;
        while (index < line_len)
        {
            if (line[index] == ' ')
            {
                index++;
                isFirst = false;
                continue;
            }
            if (isFirst)
                s1.push_back(line[index]);      
            
            else
                s2.push_back(line[index]);
                    // push_back copies the line[index] and moves forward
            
            index++;

        }
        if (isImpefectPalindrome(s1))
            cout << "yes ";
        
        else 
            cout << "no ";

        if (isImpefectPalindrome(s2))
            cout << "yes ";

        else 
            cout << "no ";

        if (isSuperAnagram(s1, s2))
            cout << "yes" << endl;
        
        else
            cout << "no" << endl;
        
    }
    file.close();
    cin.get();      // For my console, it does not function properly otherwise
}


int main()
{
    program();
    return 0;
}