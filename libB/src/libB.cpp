
#include "../include/libB.h"
#include "libC.h"
#include <iostream>
using namespace std;

int lib_b_function(){
    cout << "Library B doing some things and calling to library C:" << endl;
    lib_c_function();
    return 0;
}
