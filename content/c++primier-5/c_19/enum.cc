
#include <string>

using std::string;

#include <cstddef>

using std::size_t;

// forward declaration of unscoped enum named intValues 
enum intValues : unsigned long long; // unscoped, must specify a type
enum class open_modes;  // scoped enums can use int by default

enum class open_modes {
    input, output, append
};

// input is an enumerator of open_modes
open_modes om = open_modes::input;

enum class intTypes {
    charTyp = 8, shortTyp = 16, intTyp = 16,
    longTyp = 32, long_longTyp = 64
};

constexpr intTypes charbits = intTypes::charTyp;

enum intValues : unsigned long long {
    charTyp = 255, shortTyp = 65535, intTyp = 65535,
    longTyp = 4294967295UL,
    long_longTyp = 18446744073709551615ULL
};

int main() {
    enum color {
        red, yellow, green
    };      // unscoped enumeration
    enum class peppers {
        red, yellow, green
    }; // enumerators are hidden

    // unnamed, unscoped enum
    enum {
        floatPrec = 6, doublePrec = 10, double_doublePrec = 10
    };

    // enumerators are in scope for an unscoped enumeration
    color eyes = green;

    color hair = color::red;   // we can explicitly access the enumerators
    peppers p2 = peppers::red; // using red from peppers

    int i = color::red;   // unscoped enumerator implicitly converted to int

    // point2d is 2, point2w is 3, point3d is 3, point3w is 4
    enum class Points {
        point2d = 2, point2w,
        point3d = 3, point3w
    };

    return 0;
}
