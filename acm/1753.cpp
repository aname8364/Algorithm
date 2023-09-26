#include <iostream>
#include <vector>
#include <queue>

#define INF 99999999

using namespace std;

vector<int> dijkstra(int start, int V, vector<pair<int,int>> adj[]) {
    vector<int> dist(V + 1, INF); // V + 1 크기로 벡터 초기화
    priority_queue<pair<int, int>> pq;
    
    dist[start] = 0;
    pq.push(make_pair(0, start));
 
    while (!pq.empty()) {
        int cost = -pq.top().first;
        int cur = pq.top().second;
        pq.pop();
 
        for (auto edge : adj[cur]) { // 범위 기반 루프 사용
            int next = edge.first;
            int nCost = cost + edge.second;
            if (nCost < dist[next]) {
                dist[next] = nCost;
                pq.push(make_pair(-nCost, next));
            }
        }
    }
    
    return dist;
}

int main() {
    int V, E, K;
    cin >> V >> E >> K;
    
    vector<pair<int, int>> adj[V + 1];
    
    while (E--) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back(make_pair(v, w));
    }
    
    vector<int> dist = dijkstra(K, V, adj);
    for (int i = 1; i <= V; i++) {
        if (dist[i] == INF) { cout << "INF\n"; }
        else { cout << dist[i] << "\n"; }
    }
    
    return 0;
}
