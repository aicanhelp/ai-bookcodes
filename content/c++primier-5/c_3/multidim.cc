
#include <iterator>
using std::begin; using std::end;

#include <vector>
using std::vector;
#include <iostream>
using std::cout; using std::endl;

#include <cstddef>
using std::size_t;

int main()
{
	// array of size 3; each element is an array of 4 uninitailzed ints 
	int ia1[3][4];
	
	// array of size 10; each element is a 20-element array 
	// whose elements are arrays of 30 ints
	int arr[10][20][30] = {0}; // initialize all elements to 0
	
	// assigns the first element of arr to the last element 
	// in the last row of ia
	ia1[2][3] = arr[0][0][0];
	
	// binds row to the second four-element array in ia 
	int (&row)[4] = ia1[1];
	
	// three elements, each element is an array of size 4
	int ia2[3][4] = { 
	    {0, 1, 2, 3},   // initializers for the row indexed by 0
	    {4, 5, 6, 7},   // initializers for the row indexed by 1
	    {8, 9, 10, 11}  // initializers for the row indexed by 2
	};
	
	// equivalent initialization without the optional 
	// nested braces for each row
	int ia3[3][4] = {0,1,2,3,4,5,6,7,8,9,10,11};
	
	// explicitly initialize only element 0 in each row
	int ia4[3][4] = {{ 0 }, { 4 }, { 8 }};
	
	// explicitly initialize row 0; the remaining elements 
	// are value initialized
	int ix[3][4] = {0, 3, 6, 9};
	
	// prints 9 0 0 
	cout << ix[0][3] << ' ' << ix[1][0] << ' ' << ix[2][0] << endl;
	
	constexpr size_t rowCnt = 3, colCnt = 4;
	int ia[rowCnt][colCnt];   // 12 uninitialized elements 
	
    // for each row
    for (size_t i = 0; i != rowCnt; ++i) {
        // for each column within the row
        for (size_t j = 0; j != colCnt; ++j) {
            // assign the element's positional index as its value
            ia[i][j] = i * colCnt + j;   
		}
	}

	// four ways to print the contents of ia
	// 1. using nested range for loops
	for (const auto &row : ia) // for every element in the outer array
		for (auto col : row)   // for every element in the inner array
			cout << col << endl; // print the element's value
    cout << ia[0][0] << ' ' << ia[2][3] << endl; // prints 0 11


	// 2. using pointers and a traditional for loop
	//    with pointer arithmetic to calculate the end pointers 
	for (auto p = ia; p != ia + rowCnt; ++p) {
		// q points to the first element of an array of four ints; 
		// that is, q points to an int
	    for (auto q = *p; q != *p + colCnt; ++q)
	         cout << *q << ' ';
		cout << endl;
	}
	
	// 3. using pointers and a traditional for loop
	//    with the library begin and end functions to manage the pointers
	for (auto p = begin(ia); p != end(ia); ++p) {
		// q points to the first element in an inner array
		for (auto q = begin(*p); q != end(*p); ++q)
			cout << *q << ' ';  // prints the int value to which q points
		cout << endl;
	}
	
	// 4. using a type alias to declare the loop control variable
	using int_array = int[4]; // new style type alias declaration 

	for (int_array *p = ia; p != ia + 3; ++p) {
	    for (int *q = *p; q != *p + 4; ++q)
	         cout << *q << ' ';
		cout << endl;
	}

	// alternative way to assign positional index to elements 
	// in a two-dimensional array
	int alt_ia[rowCnt][colCnt]; // 12 uninitialized elements 
	size_t cnt = 0;
	for (auto &row : alt_ia)    // for every element in the outer array
		for (auto &col : row) { // for every element in the inner array
			col = cnt;          // give this element the next value
			++cnt;              // increment cnt
		}
	// now print the value of the array
	for (const auto &row : alt_ia) // for every element in the outer array
		for (auto col : row)     // for every element in the inner array
			cout << col << endl;

	return 0;
}
