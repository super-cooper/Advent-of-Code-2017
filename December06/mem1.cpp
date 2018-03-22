#include <iostream>
#include <cstring>
#include <vector>
#include <unordered_set>
#include <limits>

int main() {
    std::vector<int> blocks;
    char s[100];
    scanf("%[^\n]", s);
    char *s2 = strdup(s);
    char *x = strtok(s2, "\t");
    blocks.emplace_back(strtol(x, nullptr, 10));
    while ((x = strtok(nullptr, "\t")) != nullptr) {
        blocks.emplace_back(strtol(x, nullptr, 10));
    }
    free(s2);
    struct hash_vec {
        size_t operator()(std::vector<int> const &v) const {
            size_t h = 0;
            for (auto &i : v) {
                h ^= std::hash<int>()(i);
            }
            return h;
        }
    };
    std::unordered_set<std::vector<int>, hash_vec> seen(0);
    std::vector<int> curr(blocks);
    int steps = 0;
    while (seen.find(curr) == seen.end()) {
        seen.emplace(std::vector<int>(curr));
        int largest = std::numeric_limits<int>::min();
        int i = -1;
        for (int v = 0; v < (int) blocks.size(); v++) {
            if (blocks[v] > largest) {
                i = v;
                largest = blocks[v];
            }
        }
        int hold = blocks[i];
        blocks[i] = 0;
        while (hold > 0) {
            i = i != ((int) (blocks.size() - 1)) ? i + 1 : 0;
            blocks[i]++;
            hold--;
        }
        steps++;
        curr = std::vector<int>(blocks);
    }
    std::cout << steps << std::endl;
}