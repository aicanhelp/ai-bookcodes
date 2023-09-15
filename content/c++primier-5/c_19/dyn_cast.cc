
#include <typeinfo>

using std::bad_cast;

#include <iostream>

using std::cout;
using std::endl;

struct A {
    virtual ~A() {}
};

struct B : virtual public A { /* . . . */ };
struct C : public B { /* . . . */ };
struct D : public B, virtual public A { /* . . . */ };

void exercises() {
    A *pa = new C;
    if (B *pb = dynamic_cast< B * >(pa))
        cout << "cast from C to B* ok" << endl;
    else
        cout << "cast from C to B* not ok" << endl;
    B *pb = new B;
    if (C *pc = dynamic_cast< C * >(pb))
        cout << "cast from B to C* ok" << endl;
    else
        cout << "cast from B to C* not ok" << endl;

    A *pc = new C;
    if (B *pb = dynamic_cast< B * >(pc))
        cout << "cast C to B* ok" << endl;
    else
        cout << "cast C to B* not ok" << endl;

    A *pd = new D;
    if (B *pb = dynamic_cast< B * >(pd))
        cout << "cast D to B* ok" << endl;
    else
        cout << "cast D to B* not ok" << endl;
}

struct Base {
    virtual ~Base() {};
};

struct Derived : public Base {
};

void cast_to_ref(const Base &b) {
    try {
        const Derived &d = dynamic_cast<const Derived &>(b);
        // use the Derived object to which b referred
    } catch (bad_cast) {
        cout << "called f with an object that is not a Derived" << endl;
    }
}

int main() {
    Base *bp;
    bp = new Derived;  // bp actually points to a Derived object
    if (Derived *dp = dynamic_cast<Derived *>(bp)) {
        // use the Derived object to which dp points
    } else {  // bp points at a Base object
        // use the Base object to which bp points
    }

    exercises();

    cast_to_ref(*bp);
    cast_to_ref(Base());
}

