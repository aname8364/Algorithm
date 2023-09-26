#include <iostream>
#include <vector>
#include <queue>

#define MAX 100001

using namespace std;

vector<int> dijkstra(int start, int n, const vector<pair<int, int>> adj[]) {
    vector<int> dist(n+1, MAX);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    
    dist[start] = 0;
    pq.push(make_pair(0, start));
    
    while (!pq.empty()) {
        int cost = pq.top().first;
        int cur  = pq.top().second;
        pq.pop();
        
        if (cost > dist[cur]) { continue; }
        
        for (auto edge: adj[cur]) {
            int next = edge.first;
            int next_cost = cost + edge.second;
            
            if (next_cost < dist[next]) {
                dist[next] = next_cost;
                pq.push(make_pair(next_cost, next));
            }
        }
    }
    return dist;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    
    int n, k;
    cin >> n >> k;
    
    vector<pair<int, int>> adj[MAX];
    
    for (int i=0; i<=100000; i++) {
        if (i+1 <= 100000) { adj[i].push_back({i+1, 1}); }
        if (i-1 >= 0) { adj[i].push_back({i-1, 1}); }
        if (i*2 <= 100000) { adj[i].push_back({i*2, 0}); }
    }
    
    vector<int> dist = dijkstra(n, 100000, adj);
    cout << dist[k];
    
}
