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
        int inst = insts[i];
        insts[i] += inst < 3 ? 1 : -1;
        i += inst;
        steps++;
    }
    std::cout << steps << std::endl;
}
