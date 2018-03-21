#include <iostream>
#include <vector>
#include <cstring>
#include <set>
#include <algorithm>

int main() {
    std::string s;
    int count = 0;
    while (getline(std::cin, s)) {
        std::vector<std::string> v;
        char *cpy = strdup(s.c_str());
        char *x = strtok(cpy, " \t");
        v.emplace_back(x);
        while ((x = strtok(nullptr, " \t")) != nullptr) {
            v.emplace_back(x);
        }
        free(cpy);
        std::vector<std::string> v2 = std::vector<std::string>(v);
        for (auto &t : v2)
            std::sort(t.begin(), t.end());
        count += v.size() == std::set<std::string>(v2.begin(), v2.end()).size();
    }
    std::cout << count << std::endl;
}