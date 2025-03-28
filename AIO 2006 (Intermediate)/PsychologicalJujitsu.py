# https://orac2.info/problem/24/
def max_margin():
    opponent_bids = [int(input().strip()) for _ in range(13)]
    cts = {opponent_bids[i]: i + 1 for i in range(13)}
    
    highscore = 0
    for i in range(13, 0, -1):
        score = 0
        en = cts[i]
        
        for j in range(i - 1, 0, -1):
            score += cts[j]
        
        diff = score - en
        if diff > highscore:
            highscore = diff
    
    print(highscore)
 
if __name__ == "__main__":
    max_margin()
