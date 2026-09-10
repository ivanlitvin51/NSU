#include "hypo.hpp"
#include <cmath>

double hypotenuse(int a, int b) {
    return std::hypot(double(a), double(b));
}