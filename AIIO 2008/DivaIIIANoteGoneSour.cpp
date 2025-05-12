// https://orac2.info/problem/144/
#include <bits/stdc++.h>
using namespace std;
 
int main() {
    ifstream fin("divain.txt");
    ofstream fout("divaout.txt");
 
    int N, T, K;
    fin >> N >> T;
    fin >> K;
 
    map<int, vector<pair<int, int>>> events_by_day;  // day -> list of (musician, effect)
 
    for (int i = 0; i < K; ++i) {
        int d, m, r;
        fin >> d >> m >> r;
        events_by_day[d].emplace_back(m, r);
    }
 
    vector<int> current_effect(N + 1, 0);  // current slope for each musician
    vector<int> last_effect(N + 1, 0);     // effect before the latest change
 
    long long current_quality = 0;
    long long slope = 0;
    int last_day = 0;
 
    // Store all unique days to process (events + T + 1 to close the interval)
    set<int> important_days;
    for (const auto& [day, _] : events_by_day) important_days.insert(day);
    important_days.insert(T + 1);  // to finalize till end
 
    int best_day = 0;
    long long best_quality = 0;
 
    for (int day : important_days) {
        int delta_days = day - last_day;
        current_quality += slope * delta_days;
 
        // If equal quality, prefer the LATEST such day
        if (current_quality >= best_quality) {
            best_quality = current_quality;
            best_day = day - 1;
        }
 
        // Apply all effect changes at current day
        for (auto& [musician, new_r] : events_by_day[day]) {
            slope -= current_effect[musician];
            current_effect[musician] = new_r;
            slope += current_effect[musician];
        }
 
        last_day = day;
    }
 
    fout << best_day << " " << best_quality << '\n';
    return 0;
}

// approach was APPARENTLY too memory inneficient in python
