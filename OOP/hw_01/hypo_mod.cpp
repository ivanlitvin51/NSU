#include "hypo_mod.hpp"
#include "hypo.hpp"
#include <random>

static std::random_device rnd;

double hypotenuse_mod(int a, int b) {
    double res = hypotenuse(a, b);

    if (rnd() % 2 == 0) {
        res += rnd() % 10 + 1;
    }

    return res;
}
