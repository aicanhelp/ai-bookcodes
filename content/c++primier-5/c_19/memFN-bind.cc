
#include <string>

using std::string;

#include <vector>

using std::vector;

#include <iostream>

using std::cout;
using std::endl;

#include <algorithm>

using std::find_if;

#include <functional>

using std::bind;
using std::placeholders::_1;

int main() {
    vector<string> svec = {"hi", "bye"};
    // bind each string in the range to the implicit first argument to empty
    auto it = find_if(svec.begin(), svec.end(),
                      bind(&string::empty, _1));
    if (it == svec.end())
        cout << "worked" << endl;
    else
        cout << "failed" << endl;
    auto f = bind(&string::empty, _1);
    f(*svec.begin()); // ok: argument is a string f will use .* to call empty
    f(&svec[0]); // ok: argument is a pointer to string f will use .-> to call empty
}


