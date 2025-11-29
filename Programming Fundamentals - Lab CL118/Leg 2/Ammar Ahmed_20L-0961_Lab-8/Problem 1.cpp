#include <iostream>
using namespace std;

// Problem 1

void twoSum(int nums[50], int target)
{
    int finalarray[3];
    for (int i = 0; i < 50 - 1; i++)			// traversing
    {
        for (int j = 1; j < 50; j++)			// traversing
        {
            if (target == nums[i] + nums[j])    // will evaluate to desired target
            {
                finalarray[0] = nums[i];
                finalarray[1] = nums[j];
                
                for (int k = 0; k < 3; k++)
                    cout << finalarray[k] << " ";
            }                                   // program does not function till this point, for no reason
                                                // my logic is even legible !!
        }
    }


}

int main()
{
    int nums[50], size, target;
    cout << "enter size\n";
    cin >> size;
    cout << "enter nums \n";
    for (int i = 0; i < size; i++)
        cin >> nums[i];
    cout << "enter target answer\n";
    cin >> target;
    
    twoSum(&nums[50], target);

    return 0;
}