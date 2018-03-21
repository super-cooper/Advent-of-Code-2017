#include <iostream>
#include <vector>
#include <cstring>
#include <set>

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
        count += v.size() == std::set<std::string>(v.begin(), v.end()).size();
    }
    std::cout << count << std::endl;
}