# https://orac2.info/problem/272/
import heapq
 
def solve():
    # Read number of countries
    n = int(input().strip())
    if n == 0:
        print(0)
        return
    
    # Read delegates per country
    delegates = list(map(int, input().split()))
    
    # Read number of restaurants
    m = int(input().strip())
    if m == 0:
        print(sum(delegates))
        return
    
    # Read restaurant seat capacities
    seats = list(map(int, input().split()))
 
    # Sort delegates in descending order (greedy country allocation)
    delegates.sort(reverse=True)
    
    # Max heap for restaurant capacities (negative values for max heap behavior)
    seats = [-s for s in seats]
    heapq.heapify(seats)  # Convert to a min-heap (negative values act as max-heap)
 
    total_seated = 0
 
    # Try to seat each country
    for country_delegates in delegates:
        used_restaurants = []
        for _ in range(country_delegates):
            if not seats:
                break  # No restaurants left
 
            # Get the restaurant with the most seats available
            largest_seat = -heapq.heappop(seats)
 
            # If no more seats, stop
            if largest_seat == 0:
                break
            
            total_seated += 1
            largest_seat -= 1  # Use one seat
 
            if largest_seat > 0:
                used_restaurants.append(-largest_seat)  # Add back with updated capacity
 
        # Push remaining available seats back into heap
        for seat in used_restaurants:
            heapq.heappush(seats, seat)
 
    # Compute unseated delegates
    unseated_delegates = sum(delegates) - total_seated
    print(unseated_delegates)
solve()
