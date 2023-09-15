
#include <iostream>
using std::cin; using std::cout; using std::endl;

#include <string>
using std::string;

#include <vector>
using std::vector;

vector<unsigned> grades;

int main()
{
	unsigned i;
	while (cin >> i)
		grades.push_back(i);

	for (auto grade : grades) {  // for each grade in grades
		// set the initial grade as pass or fail
		string finalgrade = (grade < 60) ?  "fail" : "pass";

		finalgrade = (grade > 90) ? "high pass"
				                  : (grade < 60) ? "fail" : "pass";

		cout << grade << " " + finalgrade << endl;
	}

	return 0;
}
