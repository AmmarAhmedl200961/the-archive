#include <iostream>
using namespace std;

// Problem 5

void stats(int num)
{
    float average;
    int count = 0, sum = 0, min = 0, max = 0;
    bool first = true;

    cout << "Please enter numbers\n";

    while (true)
    {
        cin >> num;

        if (num < 0)
            break;
        
        else
        {
            if (first) {
                first = false;
                min = max = num;
            }
            if (num > max)
                max = num;
            if (num < min)
                min = num;


            sum += num;

            count++;
        }
    }
    average = 1.0 * sum / count;

    cout << "Sum = " << sum << endl;

    cout << "Average = " << average << endl;



    cout << "Maximum = " << max << endl;
    cout << "Minimum = " << min << endl;

}

int main()
{
    int num = 0;
    stats(num);

	return 0;
}