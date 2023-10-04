#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

vector<int> distances;

struct Edge {
    int start, end, weight;
};

void solve() {
    int N, M;
    cin >> N >> M;

    vector<Edge> graph(M);
    distances.assign(N, numeric_limits<int>::max());
    distances[0] = 0;

    for (int i = 0; i < M; i++) {
        int a, b, w;
        cin >> a >> b >> w;
        graph[i] = {a - 1, b - 1, w};
    }

    for (int i = 0; i < N - 1; i++) {
        for (const auto& edge : graph) {
            int start = edge.start;
            int end = edge.end;
            int weight = edge.weight;
            int newWeight = weight + distances[start];
            if (distances[start] != numeric_limits<int>::max() && newWeight < distances[end]) {
                distances[end] = newWeight;
            }
        }
    }

    for (int i = 0; i < N; i++) {
        if (distances[i] == numeric_limits<int>::max()) {
            distances[i] = 30000;
        }
    }

    for (int i = 0; i < N; i++) {
        cout << distances[i] << " ";
    }
    cout << endl;
}

int main() {
    int T = 1;
    while (T--) {
        solve();
    }
    return 0;
}
