
#include "Sales_item.h"
#include <iostream>
#include <string>

int main() {

	int v1(1024);    // direct-initialization, functional form
	int v2{1024};    // direct-initialization, list initializer form
	int v3 = 1024;   // copy-initialization
	int v4 = {1024}; // copy-initialization, list initializer form


	// alternative ways to initialize string from a character string literal
	std::string titleA = "C++ Primer, 5th Ed.";
	std::string titleB("C++ Primer, 5th Ed.");
	std::string all_nines(10, '9');  // all_nines = "9999999999"

	return 0;
}
