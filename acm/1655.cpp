#include <iostream>
#include <queue>

using namespace std;

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    int n;
    std::cin >> n;
    
    std::priority_queue<int, vector<int>, less<int>>    max_pq;
    std::priority_queue<int, vector<int>, greater<int>> min_pq;
    
    for (int i=1; i<n+1; i++) {
        int x;
        std::cin >> x;
        
        if (i%2 == 0) { min_pq.push(x); }
        else { max_pq.push(x); }
        
        if (!max_pq.empty() && !min_pq.empty()) {
            int max_top = max_pq.top();
            int min_top = min_pq.top();
                
            if (max_top > min_top) {
                min_pq.push(max_top);
                max_pq.pop();
                max_pq.push(min_top);
                min_pq.pop();
            }
        }
        cout << max_pq.top() << "\n";
        
    }
}