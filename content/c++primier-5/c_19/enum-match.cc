
#include <iostream>

using std::cout;
using std::endl;

// unscoped enumeration; the underlying type is machine dependent
enum Tokens {
    INLINE = 128, VIRTUAL = 129
};

void ff(Tokens) {
    cout << "ff(Tokens)" << endl;
}

void ff(int) {
    cout << "ff(int)" << endl;
}

void newf(int) {
    cout << "newf(int)" << endl;
}

void newf(unsigned char) {
    cout << "newf(unsigned char)" << endl;
}

int main() {
    Tokens curTok = INLINE;
    ff(128);    // exactly matches ff(int)
    ff(INLINE); // exactly matches ff(Tokens)
    ff(curTok); // exactly matches ff(Tokens)

    void newf(unsigned char);
    void newf(int);
    unsigned char uc = VIRTUAL;

    newf(VIRTUAL);  // calls newf(int)
    newf(uc);       // calls newf(unsigned char)

    newf(129);      // calls newf(int)

    return 0;
}
