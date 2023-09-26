#include <iostream>
#include <vector>
#include <queue>

#define MAXCOST 100000001

using namespace std;

vector<int> dijkstra(int start, int n, const vector<pair<int, int>> adj[]) {
    vector<int> dist(n+1, MAXCOST);
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

    int n, m;
    cin >> n >> m;
    
    vector<pair<int, int>> adj[n+1];
    
    for (int i=0; i<m; i++) {
        int x, y, z;
        cin >> x >> y >> z;
        adj[x].push_back(make_pair(y, z));
    }
    
    int start, end;
    cin >> start >> end;
    
    vector<int> dist = dijkstra(start, n, adj);
    
    cout << dist[end];
}
