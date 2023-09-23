#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <numeric>

std::pair<int, int> getFirstOdd(const std::vector<int>& vec) {
    for (int i=0; i<vec.size(); i++) {
        if (vec[i]%2 != 0) { return std::make_pair(vec[i], i); }
    }
    return std::make_pair(-1, -1);
}

int main() {
    std::cin.tie(0);
    std::cout.tie(0);
    std::ios_base::sync_with_stdio(false);
    
    int n;
    std::cin >> n;
    
    std::vector<int> vec(n);
    
    for (int i=0; i<n; i++) {
        std::cin >> vec[i];
    }
    
    std::sort(vec.begin(), vec.end());
    
    auto total = std::accumulate(vec.begin(), vec.end(), 0);
    
    while (total%2 != 0) {
        if (vec.empty()) { total = 0; }
        else {
            std::pair<int, int> firstOdd = getFirstOdd(vec);
            total -= firstOdd.first;
            vec.erase(vec.begin() + firstOdd.second);
        }
    }
    std::cout << total << std::endl;
}