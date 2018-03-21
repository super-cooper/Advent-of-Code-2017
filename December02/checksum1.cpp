#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

int main() {
    vector<vector<int>> puzzle;
    string s;
    while (getline(cin, s)) {
        vector<int> line;
        char *cpy = strdup(s.c_str());
        char *x = strtok(cpy, "\t");
        line.push_back((int) strtol(x, nullptr, 10));
        while ((x = strtok(nullptr, "\t")) != nullptr) {
            line.push_back((int) strtol(x, nullptr, 10));
        }
        free(cpy);
        puzzle.push_back(line);
    }
    int count = 0;
    for (vector<int> line : puzzle) {
        int max = *max_element(line.begin(), line.end());
        int min = *min_element(line.begin(), line.end());
        count += max - min;
    }
    cout << count << endl;
}
