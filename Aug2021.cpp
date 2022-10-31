#include <random>
#include <iostream>

int main() {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0.0, 1.0);

    unsigned long robot_1_wins = 0;
    unsigned long robot_2_wins = 0;

    for (int n = 0; n < 1e10; ++n) {
        while (true) {
            double sum = dis(gen);
            if (sum > 0.5) {
                ++robot_1_wins;
                break;
            }
            sum -= dis(gen);
            if (sum < -0.5) {
                ++robot_2_wins;
                break;
            }
        }
    }
    std::cout << "robot_1_wins = " << robot_1_wins << std::endl;
    std::cout << "robot_2_wins = " << robot_2_wins << std::endl;
}