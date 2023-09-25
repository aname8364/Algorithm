#include <iostream>
#include <queue>

int main() {
    int n;
    std::cin >> n;
    
    std::priority_queue<int, std::vector<int>, std::greater<int>> pq;
    
    for (int i=0; i<n; i++) {
        int cards;
        std::cin >> cards;
        
        pq.push(cards);
    }
    
    int total = 0;
    while (pq.size() != 1) {
        int card1 = pq.top();
        pq.pop();
        int card2 = pq.top();
        pq.pop();
        int sum = card1 + card2;
        total += sum;
        pq.push(sum);
    }
    std::cout << total << "\n";
}