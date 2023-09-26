#include <iostream>
#include <vector>
#include <queue>

#define MAX 1000001

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
    
    int n, m, x;
    cin >> n >> m >> x;
    
    vector<pair<int, int>> adj[n+1];
    
    for (int i=0; i<m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        adj[a].push_back({b, c});
    }
    
    vector<int> in_dist = dijkstra(x, n, adj);
    
    vector<int> out_dist;
    int long_cost = 0;
    
    for (int i=1; i<=n; i++) {
        out_dist = dijkstra(i, n, adj); 
        long_cost = max(long_cost, out_dist[x] + in_dist[i]);
    }
    
    cout << long_cost;
    
}
