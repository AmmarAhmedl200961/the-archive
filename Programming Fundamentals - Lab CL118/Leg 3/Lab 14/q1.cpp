#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() 
{
	vector<int>v(10);

	for (int i = 1; i <= 3; i++)
		v.push_back(i);

	cout << "v.size() after push_back thrice " << v.size() << endl;

	// values
	for (int i = 0; i < v.size(); i++)
		cout << v[i] << " ";

	for (int i = 0; i < 2; i++)
		v.pop_back();

	cout << endl;

	cout << "v.size() after pop_back twice " << v.size() << endl;

	cout << "v.max_size() " << v.max_size() << endl;

	// last index value
	// v.at method
	cout << v.at(v.size()-1) << endl;

	// array method
	cout << v[v.size() - 1] << endl;

	// last index + 1 value
	// v.at method
	cout << v.at(v.size() - 2) << endl;

	// array method
	cout << v[v.size() - 2] << endl;

	v.insert(v.begin(), 100);
	cout << "Inserted value 100 at beginning " << *v.begin() << endl;
	v.erase(v.begin());
	cout << "Erased value 100 at beginning " << *v.begin() << endl;

	// cleared vector
	v.clear();
	cout << "Vector Cleared " << endl;

	return 0;
}