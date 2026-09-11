#include "hypo_mod.hpp"
#include "hypo.hpp"
#include <random>

double hypotenuse_mod(int a, int b) {
    // 1. Генератор псевдослучайных чисел (Mersenne Twister),
    // инициализируемый зерном от железа/ОС один раз при первом вызове
    static std::mt19937 gen(std::random_device{}());

    // 2. Равномерные распределения (математически честные, без смещения остатка)
    static std::uniform_int_distribution<int> coin(0, 1);    // 50% шанс модификации (0 или 1)
    static std::uniform_int_distribution<int> bonus(1, 10);  // прибавка от 1 до 10 включительно

    double res = hypotenuse(a, b);

    if (coin(gen) == 0) {
        res += bonus(gen);
    }

    return res;
}
