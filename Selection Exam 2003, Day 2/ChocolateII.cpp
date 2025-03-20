// https://orac2.info/problem/260/
#include "beam.h"
#include <vector>
#include <algorithm>
 
using namespace std;
 
// Function to find all coin locations using divide-and-conquer and binary search
void findCoins(int left, int right, int totalCoins) {
    if (totalCoins == 0) return; // No coins in this range
 
    if (left == right) {
        // Only one location, and it must contain a coin
        collect(left);
        return;
    }
 
    int mid = (left + right) / 2;
 
    // Count coins in the left half [left, mid]
    int leftCoins = shine(left, mid);
 
    // Recursively find coins in the left half
    findCoins(left, mid, leftCoins);
 
    // Count coins in the right half [mid+1, right]
    int rightCoins = totalCoins - leftCoins;
 
    // Recursively find coins in the right half
    findCoins(mid + 1, right, rightCoins);
}
 
void init() {
    // Get the width of the vending machine
    int n = machineWidth();
 
    // Count the total number of coins under the vending machine
    int totalCoins = shine(1, n);
 
    // Find all coin locations
    findCoins(1, n, totalCoins);
}