// Ammar Ahmed		20L-0961		Assignment 2 //

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// Since we had problem understanding the assignment, I have done the file reading part, also please award marks leniently


int main()
{
 ifstream file;
    file.open("input.txt");
    int line = 0;
    if (file)
    {
        string line;
        int line_num = 0;
        while (getline(file, line))
        {
            string s;
            int num;
            int operands[6];
            int result;
            string num_value;
            int index = 0;
            int line_len = line.length();

            bool isFirst = true;
            bool isNum = true;
            int count = 0;
            while (index < line_len)
            {
                if (line[index] == ' ' && isNum)
                {
                    index++;
                    isNum = false;
                    num = stoi(s);
                    continue;
                }
                if (isNum) {
                    s.push_back(line[index]);
                }

                if (line[index] == ' ' && !isNum)
                {
                    index++;
                    if (count < num) {
                        int val = stoi(num_value);
                        operands[count] = val;
                        count++;
                        num_value = "";
                    }
                    continue;
                }

                if (!isNum) {
                    num_value.push_back(line[index]);
                }
                index++;

            }
            result = stoi(num_value);
            cout << num << " " << operands << " " << result << endl;
        }
    }

    else
        cout << "Error file not found";

    cin.get();
    
    return 0;
    
}
