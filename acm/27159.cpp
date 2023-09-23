#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    
    std::vector<int> cards;
    int total = 0;
    
    for (int i=0; i<n; i++) {
        int x;
        std::cin >> x;
        
        if (cards.empty()) {
            total += x;
        }
        else if (x - cards.back() != 1) total += x;
        cards.push_back(x);
    }
    
    std::cout << total;
    
}