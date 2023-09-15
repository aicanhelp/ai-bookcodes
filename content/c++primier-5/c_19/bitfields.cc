
#include <iostream>

using std::cout;
using std::endl;

typedef unsigned int Bit;

class File {
    Bit mode: 2;       // mode has 2 bits
    Bit modified: 1;   // modified has 1 bit
    Bit prot_owner: 3; // prot_owner has 3 bits
    Bit prot_group: 3; // prot_group has 3 bits
    Bit prot_world: 3; // prot_world has 3 bits
    // operations and data members of File
public:
    // file modes specified as octal literals; see XREF(intLiterals)
    enum modes {
        READ = 01, WRITE = 02, EXECUTE = 03
    };

    File &open(modes);

    void close();

    void write();

    bool isRead() const;

    void setWrite();

    void execute();

    bool isExecute() const;
};

void File::write() {
    modified = 1;
    // . . .
}

void File::close() {
    if (modified)
        // . . . save contents
        ;
}

inline bool File::isRead() const { return mode & READ; }

inline void File::setWrite() { mode |= WRITE; }


File &File::open(File::modes m) {
    mode |= READ;    // set the READ bit by default
    // other processing
    if (m & WRITE) // if opening READ and WRITE
        // processing to open the file in read/write mode
        cout << "myFile.mode READ is set" << endl;
    return *this;
}

int main() {
    File myFile;

    myFile.open(File::READ);
    if (myFile.isRead())
        cout << "reading" << endl;

    return 0;
}

