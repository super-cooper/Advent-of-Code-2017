#include <iostream>
#include <unordered_map>
#include <functional>

#define solve(num) ((num) > target ? (num) : 0)
#define hash(x) (std::hash<size_t>()(x))

typedef struct {
    template <class T1, class T2>
    std::size_t operator () (const std::pair<T1,T2> &p) const {
        auto h1 = std::hash<T1>{}(p.first);
        auto h2 = std::hash<T2>{}(p.second);

        return hash(h1) & hash(h2);
    }
} pair_hash;
typedef std::unordered_map<std::pair<int, int>, int, pair_hash> coord_map;

int sum_adj(std::pair<int, int> &xy, coord_map *coords) {
    int x = xy.first;
    int y = xy.second;
    int count = 0;
    int vals[8] = {
            (*coords)[{x - 1, y}],
            (*coords)[{x + 1, y}],
            (*coords)[{x, y - 1}],
            (*coords)[{x, y + 1}],
            (*coords)[{x - 1, y - 1}],
            (*coords)[{x - 1, y + 1}],
            (*coords)[{x + 1, y - 1}],
            (*coords)[{x + 1, y + 1}]
    };
    for (int v : vals)
        count += v;
    return count;
}

int main() {
    int target;
    std::cin >> target;
    coord_map vals = coord_map({{{0, 0}, 1}});
    int x = 0;
    int y = 0;
    int row = 1;
    int val = 0;

    while (val == 0) {
        while (x < row && !val) {
            std::pair<int, int> xy = {++x, y};
            int num = sum_adj(xy, &vals);
            vals[xy] = num;
            val = solve(num);
        }
        while (y < row && !val) {
            std::pair<int, int> xy = {x, ++y};
            int num = sum_adj(xy, &vals);
            vals[xy] = num;
            val = solve(num);
        }
        while (x > -row && !val) {
            std::pair<int, int> xy = {--x, y};
            int num = sum_adj(xy, &vals);
            vals[xy] = num;
            val = solve(num);
        }
        while (y > -row && !val) {
            std::pair<int, int> xy = {x, --y};
            int num = sum_adj(xy, &vals);
            vals[xy] = num;
            val = solve(num);
        }
        row++;
    }
    std::cout << val << std::endl;
}
