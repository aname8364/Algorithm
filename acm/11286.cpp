#include <iostream>
#include <queue>
#include <cmath>

struct compare {
    bool operator()(int x, int y) {
        if (abs(x) != abs(y)) { return abs(x)>abs(y); }
        else { return x>y; }
    }
};

int main() {
    std::ios_base::sync_with_stdio(false); 
    std::cin.tie(NULL); 
    std::cout.tie(NULL);

    int n;
    std::cin >> n;
    
    std::priority_queue<int, std::vector<int>, compare> pq;
    
    for (int i=0; i<n; i++) {
        int x;
        std::cin >> x;
        
        if (x == 0) {
            if (pq.empty()) { std::cout << "0\n"; }
            else {
                std::cout << pq.top() << "\n";
                pq.pop();
            }
        }
        else { pq.push(x); }
    }
}