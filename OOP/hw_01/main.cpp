#include <iostream>
#include "hypo.hpp"
#include "hypo_mod.hpp"

int main() {
    int a, b;

    std::cout << "Katet A: ";
    std::cin >> a;
    std::cout << "Katet B: ";
    std::cin >> b;

    double res_1 = hypotenuse(a ,b);
    std::cout << "Default hypotenuse: " << res_1 << "\n";

    double res_2 = hypotenuse_mod(a ,b);
    std::cout << "Mod hypotenuse: " << res_2;
}