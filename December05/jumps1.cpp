#include <vector>
#include <iostream>

int main() {
    std::vector<int> insts;
    int i = 0, steps = 0;
    std::string s;
    while (getline(std::cin, s)) {
        insts.emplace_back(strtol(s.c_str(), nullptr, 10));
    }
    auto n = (int) insts.size();
    while (0 <= i && i < n) {
        i += insts[i]++;
        steps++;
    }
    std::cout << steps << std::endl;
}
