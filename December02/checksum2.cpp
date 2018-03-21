#include <cstdio>
#include <iostream>
#include <vector>
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
        for (unsigned long i = 0; i < line.size(); i++) {
            for (unsigned long j = i + 1; j < line.size(); j++) {
                if (line[i] % line[j] == 0) {
                    count += line[i] / line[j];
                } else if (line[j] % line[i] == 0) {
                    count += line[j] / line[i];
                }
            }
        }
    }
    cout << count << endl;
}
